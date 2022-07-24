from doctest import debug_script
from django.db import models

# Create your models here.

class Post(models.Model):
    # host = 
    # topic = 
    name = models.CharField(max_length=255)
    description = models.TextField(null = True, blank = True)
    # participants = 
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name