from django.test import TestCase
from .models import Customer, ChatMessage, Complaint

from django.core.management.base import CommandError
from io import StringIO
from django.core.management import call_command


class CustomerModelTests(TestCase):
    def test_str_representation(self):
        customer = Customer(name="John Doe", email="john@example.com")
        self.assertEqual(str(customer), "John Doe")


class CommandInputTests(TestCase):
    def test_invalid_email_input(self):
        out = StringIO()
        user_input = "John Doe\njohn@example\n1234567890\n123 Main St\nno\n"
        with self.assertRaises(CommandError):
            call_command("chat", stdin=StringIO(user_input), stdout=out)
            self.assertIn("Invalid email format.", out.getvalue())

    def test_complaint_summary_saved(self):
        # Assuming the command to accept 'yes' to file a complaint and simulate user input
        user_input = "John Doe\njohn@example.com\n1234567890\n123 Main St\nyes\n"
        out = StringIO()
        call_command("chat", stdin=StringIO(user_input), stdout=out)
        self.assertTrue(Complaint.objects.exists())
