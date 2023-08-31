from django.db import models
import string 
import random


# Create your models here.
def generate_uniquecode():
    leng = 6
    while True:
        code = "".join(random.choice(string.ascii_uppercase, k=leng))
        if Room.objects.filter(code=code).count()==0:
            break
    return code



class Room(models.Model):
    code = models.CharField(max_length=10, default=generate_uniquecode, unique=True)
    host = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)

