from django.db import models
import datetime

class Subscriber(models.Model):
        email = models.EmailField(max_length=50)
        first_name = models.CharField(max_length=50)
        last_name = models.CharField(max_length=50)
        date = models.DateTimeField(auto_now_add=True)