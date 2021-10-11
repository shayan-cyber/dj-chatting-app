from django.urls import path
from . import views
urlpatterns =[
    path('', views.home, name='home'),
    path('chat_room/<str:username>', views.chat_room, name='chat_room')
]