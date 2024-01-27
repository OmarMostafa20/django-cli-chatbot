from django.test import TestCase
from .models import Customer, ChatMessage, Complaint

from django.core.management.base import CommandError
from io import StringIO
from django.core.management import call_command
from unittest.mock import patch, MagicMock

from chatbot_app.chatbot import ChatBot, SummaryBot


class CustomerModelTest(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(
            name="John Doe",
            email="john@example.com",
            phone_number="1234567890",
            address="1234 Main St",
        )

    ##########################################################################################

    def test_model_creation(self):
        self.assertEqual(self.customer.name, "John Doe")
        self.assertEqual(self.customer.email, "john@example.com")
        self.assertEqual(self.customer.phone_number, "1234567890")
        self.assertEqual(self.customer.address, "1234 Main St")

    ##########################################################################################

    def test_string_representation(self):
        self.assertEqual(str(self.customer), "John Doe")


class ChatBotTest(TestCase):
    def setUp(self):
        self.chatbot = ChatBot()

    ##########################################################################################

    def test_response_generation(self):
        response = self.chatbot.get_response("Hello")
        self.assertIsNotNone(response)  # Check that a response is returned


class CommandInputTests(TestCase):
    @patch("chatbot_app.chatbot.ChatBot.get_response")
    def test_chatbot_exception_handling(self, mock_get_response):
        mock_get_response.side_effect = Exception("Test exception")

        with self.assertRaises(Exception) as context:
            call_command(f"An error occurred: {str(context)}")

        self.assertTrue("Test exception" in str(context.exception))

    ##########################################################################################

    def test_invalid_email_input(self):
        user_inputs = [
            "John Doe\ninvalid_email\n1234567890\n123 Main St\nquit\n",
            "John Doe\n\n1234567890\n123 Main St\nquit\n",
            "John Doe\njohn@example\n1234567890\n123 Main St\nquit\n",
        ]
        for user_input in user_inputs:
            with self.assertRaises(CommandError):
                call_command("chat", stdin=StringIO(user_input))

    ##########################################################################################

    def test_invalid_phone_number_input(self):
        user_inputs = [
            "John Doe\njohn@example.com\n12345\n123 Main St\nquit\n",
            "John Doe\njohn@example.com\ninvalid_number\n123 Main St\nquit\n",
        ]
        for user_input in user_inputs:
            with self.assertRaises(CommandError):
                call_command("chat", stdin=StringIO(user_input))

    ##########################################################################################

    def test_address_input(self):
        user_input = "John Doe\njohn@example.com\n1234567890\n123 Main St\nquit\n"
        out = StringIO()
        call_command("chat", stdin=StringIO(user_input), stdout=out)

    ##########################################################################################

    @patch(
        "chatbot_app.chatbot.ChatBot.get_response", return_value="Mocked Bot Response"
    )
    def test_chat_flow(self, mock_chat_response):
        user_input = (
            "John Doe\njohn@example.com\n1234567890\n123 Main St\nHello\nquit\n"
        )
        out = StringIO()
        call_command("chat", stdin=StringIO(user_input), stdout=out)
        self.assertIn("Mocked Bot Response", out.getvalue())

    ##########################################################################################

    @patch(
        "chatbot_app.chatbot.ChatBot.get_response",
        side_effect=Exception("Mocked Exception"),
    )
    def test_chat_exception_handling(self, mock_chat_response):
        user_input = (
            "John Doe\njohn@example.com\n1234567890\n123 Main St\nHello\nquit\n"
        )
        with self.assertRaises(CommandError):
            call_command("chat", stdin=StringIO(user_input))

    ##########################################################################################

    @patch(
        "chatbot_app.chatbot.ChatBot.SummaryBot.get_response",
        return_value="Mocked Summary",
    )
    def test_complaint_and_summary_creation(self, mock_summary_response):
        user_input = (
            "John Doe\njohn@example.com\n1234567890\n123 Main St\nHello\nquit\n"
        )
        call_command("chat", stdin=StringIO(user_input))
        self.assertTrue(Complaint.objects.exists())
        complaint = Complaint.objects.first()
        self.assertEqual(complaint.summary, "Mocked Summary")

    ##########################################################################################

    @patch(
        "chatbot_app.chatbot.ChatBot.SummaryBot.get_response",
        return_value="Mocked Summary",
    )
    def test_complaint_and_summary_creation(self, mock_summary_response):
        user_input = (
            "John Doe\njohn@example.com\n1234567890\n123 Main St\nHello\nquit\n"
        )
        call_command("chat", stdin=StringIO(user_input))
        self.assertTrue(Complaint.objects.exists())
        complaint = Complaint.objects.first()
        self.assertEqual(complaint.summary, "Mocked Summary")

    ##########################################################################################

    def test_console_output(self):
        user_input = "John Doe\njohn@example.com\n1234567890\n123 Main St\nquit\n"
        out = StringIO()
        call_command("chat", stdin=StringIO(user_input), stdout=out)
        output = out.getvalue()
        self.assertIn("Welcome to our CLIBot Service!", output)
