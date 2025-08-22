from django.apps import AppConfig


class ChatClientConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chat_client'
    
    def ready(self):
        # Import signals or other startup code
        pass