from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot_corpus.data import __path__ as corpus_path
import os

# Create chatbot instance with a custom storage adapter and more logical control
chatbot = ChatBot(
    'TerminalBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///db.sqlite3',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am not sure how to respond to that.',
            'maximum_similarity_threshold': 0.90
        },
        {
            'import_path': 'chatterbot.logic.MathematicalEvaluation',
        },
        {
            'import_path': 'chatterbot.logic.TimeLogicAdapter',
        }
    ],
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace',
    ]
)

def train_chatbot():
    chatbot.storage.drop()  # Clear existing database
    trainer = ChatterBotCorpusTrainer(chatbot)
    trainer.train('chatterbot.corpus.english')

# Check if training is needed
if not os.path.exists('db.sqlite3'):
    train_chatbot()
else:
    # Verify the database has data
    if not chatbot.storage.filter():
        train_chatbot()

def get_chatbot_response(user_input):
    """Get a response from the chatbot"""
    # Add specific logic for custom questions like 'What can you do?'
    if "What can you do?" in user_input:
        return "I consume RAM, and binary digits."
    elif "What did we talk about earlier?" in user_input:
        # A simple version to "remember" the last few exchanges
        # You can store and retrieve from database for persistent memory
        return "I don't have memory of past conversations yet, but I can answer your current questions!"
    else:
        return chatbot.get_response(user_input)

# Example interaction
if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        response = get_chatbot_response(user_input)
        print(f"Bot: {response}")
