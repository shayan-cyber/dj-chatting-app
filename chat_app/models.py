from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.

class Chat_group(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False)
    participants = models.ManyToManyField(User)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "chat group of : " + str(self.unique_id)


class Chat(models.Model):
    group = models.ForeignKey(Chat_group, on_delete= models.CASCADE)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name= "author")
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "chat of : " + str(self.group.unique_id) + " from " + str(self.author.username) + " time : " + str(self.time)

    
