# chatbot.py
import aiml

class Chatbot:
    def __init__(self):
        # Create an AIML kernel
        self.kernel = aiml.Kernel()
        # Load the AIML files
        self.kernel.learn("std-startup.xml")
        self.kernel.respond("load aiml b")

    def greet_user(self):
        return "👋 Hello! Welcome to InfoBuddy. I'm here to assist you. How can I help you today? 😊"

    def handle_question(self, question):
        response = self.kernel.respond(question)
        if not response:
            return "I'm sorry, I didn't understand that. Can you please rephrase?"
        return response

    def farewell_message(self):
        return "Goodbye! If you have more questions, feel free to ask later. or contact : +9189********"

    # Additional questions and responses
    def respond_to_student_details(self):
        return "Sure, I can help you with student details. Please provide more information about what you're looking for."
    
    def respond_to_purpose_of_this_chatbot(self):
        return "This Chatbot is Providing details for the farewell event."

    def respond_to_contact_information(self):
        return "Certainly! If you need contact information, could you please specify whose contact details you're interested in?"

    def respond_to_farewell_dates(self):
        return "The farewell dates are scheduled for [Provide Specific Dates]."

    def respond_to_farewell_timings(self):
        return "The farewell event will start at [Provide Specific Timings]."

    def respond_to_farewell_venue(self):
        return "The farewell will take place at [Provide Specific Venue]."

    def respond_to_guests_information(self):
        return "We expect various dignitaries and guests to attend the farewell. The confirmed guest list will be announced closer to the event."

    def respond_to_food_types(self):
        return "The menu for the farewell includes a variety of dishes such as Veg & Non-Veg ."

    def respond_to_programs(self):
        return "The farewell program will include various activities, speeches, and entertainment. The detailed schedule will be provided in the official announcement."
