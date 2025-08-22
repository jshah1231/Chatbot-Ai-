from django.core.management.base import BaseCommand
from chat_client.chatbot.chatbot import get_chatbot_response, train_chatbot

class Command(BaseCommand):
    help = 'Start a terminal chat session with ChatterBot'

    def add_arguments(self, parser):
        parser.add_argument(
            '--retrain',
            action='store_true',
            help='Force retrain the chatbot before starting'
        )

    def handle(self, *args, **options):
        if options['retrain']:
            self.stdout.write(self.style.WARNING('Retraining chatbot...'))
            train_chatbot()
            
        self.stdout.write(self.style.SUCCESS('Starting chat session...'))
        self.stdout.write("Type 'quit' to exit the chat.\n")
        
        while True:
            user_input = input("You: ")
            
            if user_input.lower() == 'quit':
                self.stdout.write(self.style.SUCCESS('Goodbye!'))
                break
                
            response = get_chatbot_response(user_input)
            self.stdout.write(f"Bot: {response}")