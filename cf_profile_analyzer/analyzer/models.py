from django.db import models


class UserName(models.Model):
    username = models.CharField(max_length=64, unique=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
