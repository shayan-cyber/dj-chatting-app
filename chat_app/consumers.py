from channels.generic.websocket import AsyncJsonWebsocketConsumer
import django
django.setup()

from . models import *

from django.contrib.auth.models import User
from channels.db import database_sync_to_async
from django.contrib.humanize.templatetags.humanize import naturaltime

class ChatConsumer(AsyncJsonWebsocketConsumer):

    @database_sync_to_async
    def save_chat(self, msg, author, groupname):
        chat_group = Chat_group.objects.get(unique_id = groupname)
        chat = Chat.objects.create(body= msg, group= chat_group, author = User.objects.get(username = author))

        return chat


    async def connect(self):
        await self.accept()

    
    async def receive_json(self,content):
        data = content
        if data['command'] == 'join':
            await self.channel_layer.group_add(
                data['groupname'],
                self.channel_name
            )
            print('added')
        if data['command'] == 'send':
            print("count")

            chat = await self.save_chat(data['message'], str(self.scope['user']), data['groupname'])
            await self.channel_layer.group_send(
                data['groupname'],
                {
                    'type':'chat.message',
                    'message':str(chat.body),
                    'groupname':str(chat.group.unique_id),
                    'author':str(chat.author.username),
                    'time':str(chat.time.strftime("%m/%d/%Y %I:%M %p")),
                }
                
            )

    async def disconnect(self,msg):
        pass

    async def chat_message(self,event):
        print("count2")
        
        
        await self.send_json(
            {
                'message':event['message'], 
                'author':event['author'],
                'time':event['time']
            }
        )


    
        
