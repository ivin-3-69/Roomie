from django.db import models

# Create your models here.
class chatdb(models.Model):
    user_id = models.IntegerField()
    time_match = models.DateTimeField(auto_now_add=True)
    message_last = models.CharField(max_length=200)
    time_update = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.message_last


