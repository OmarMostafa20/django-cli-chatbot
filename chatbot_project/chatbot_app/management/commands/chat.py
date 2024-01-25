from django.core.management.base import BaseCommand
from chatbot_app.models import Customer, ChatMessage, Complaint
from chatbot_app.chatbot import FlanT5Chatbot
import re
import uuid


class Command(BaseCommand):
    help = "Start the chatbot CLI"

    def handle(self, *args, **kwargs):
        chatbot = FlanT5Chatbot()
        print("Welcome to the Chatbot CLI. Let's begin by collecting some information.")

        # Collect customer information
        name = input("Please enter your name: ")
        email = input("Please enter your email: ")
        phone_number = input("Please enter your phone number: ")
        address = input("Please enter your address: ")

        # Validate email and phone number (basic validation)
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            print("Invalid email format.")
            return
        if not re.match(r"\d{10,15}", phone_number):
            print("Invalid phone number format.")
            return

        # Create or update customer information
        customer, created = Customer.objects.get_or_create(
            email=email,
            defaults={"name": name, "phone_number": phone_number, "address": address},
        )
        if not created:
            Customer.objects.filter(email=email).update(
                name=name, phone_number=phone_number, address=address
            )

        # Start chat loop
        print("You can start chatting now. Type 'quit' to exit.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == "quit":
                break

            response = chatbot.get_response(user_input)
            print(f"Chatbot: {response}")

            # Log chat message
            ChatMessage.objects.create(customer=customer, message=user_input)

        print("Thank you for using the chatbot. Goodbye!")

        # At the end of the chat loop in chat.py
        user_decision = input(
            "Would you like to file a complaint based on this conversation? (yes/no): "
        )
        if user_decision.lower() == "yes":
            # Here, you would integrate a summarization model or a simple placeholder
            complaint_summary = "This is a placeholder summary of the customer's issue."
            # Generate a unique complaint ID (for simplicity, using a UUID here)

            complaint_id = uuid.uuid4()
            complaint = Complaint.objects.create(
                customer=customer, summary=complaint_summary
            )
            print(f"Complaint filed. Summary: {complaint_summary}")
            print(f"Your complaint ID is: {complaint_id}")
