from django.core.management.base import BaseCommand
from chatbot_app.models import Customer, ChatMessage, Complaint
from chatbot_app.chatbot import ChatBot, SummaryBot
import re


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        ### Define Model
        chatBot = ChatBot()
        summaryBot = SummaryBot()

        #############################################################################################################

        ### Welcome Messages
        print("🌟 Welcome to our CLIBot Service! 🌟")
        print("Let's get started by gathering some basic information from you.")

        #############################################################################################################

        ### User Data

        # Name Input
        name = input("Please enter your full name: ")

        # Email Input With Validation Loop
        email = ""
        while not email:
            email_input = input("Please enter your email address: ")
            if re.match(r"[^@]+@[^@]+\.[^@]+", email_input):
                email = email_input
            else:
                print("The email address format seems incorrect. Please try again.")

        # Phone Number Input With Validation Loop
        phone_number = ""
        while not phone_number:
            phone_input = input("Please enter your phone number: ")
            if re.match(r"\d{10,15}", phone_input):
                phone_number = phone_input
            else:
                print(
                    "The phone number format seems incorrect. Please enter a valid number."
                )

        # Address Input
        address = input("Please enter your address: ")

        #############################################################################################################

        # Create Customer into DataBase
        customer, _ = Customer.objects.get_or_create(
            email=email,
            defaults={"name": name, "phone_number": phone_number, "address": address},
        )

        #############################################################################################################

        # Start Chatting

        print(
            "\n--- CLIBot ---\nHi! I'm CLIBot, Here to help you record your problems. Type 'quit' or 'exit' to end the conversation."
        )
        context = ""
        while True:
            # User Input Message
            user_input = input("\nUser: ")

            #############################################################################################################

            # User End Chat - Summarize the User's Problem using ResolveBot
            if user_input.lower() in ["exit", "quit"]:
                lines = context.split("\n")

                # Extract messages that start with "User:"
                user_messages = [
                    message.split('User: "')[1][:-1]
                    for message in lines
                    if message.startswith("User:")
                ]

                # Concatenate the messages into one string
                user_messages_concatenated = " ".join(user_messages)

                # Check the length of the concatenated messages
                if len(user_messages_concatenated) <= 150:
                    # If the messages are short enough, save them directly
                    complaint_summary = user_messages_concatenated
                else:
                    # If the messages are too long, get a summary
                    complaint_summary = summaryBot.get_response(
                        user_messages_concatenated
                    )

                # Save Summary into DataBase
                Complaint.objects.create(customer=customer, summary=complaint_summary)

                context = ""

                break

            #############################################################################################################

            # Chatting With User
            try:
                context += f'\nUser: "{user_input}'

                response = chatBot.get_response(user_input)
                print(f"ResolveBot: {response}")
                # context += f'\nResolveBot: "{response}'
                ChatMessage.objects.create(customer=customer, message=user_input)
            except Exception as e:
                print(f"Don't consider this note and continue the chat.")

        print("🌟 We hope you had a great experience. Have a wonderful day! 🌟")
