from django.urls import path
from chat_app.consumers import ChatConsumer


ws_application =[
    path('ws/chat/', ChatConsumer.as_asgi())
]