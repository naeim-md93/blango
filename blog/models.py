from django.db import models
from django.conf import settings

# Create your models here.
import os
print(os.getenviron['CODIO_HOSTNAME'])

class Tag(models.Model):
    value = models.TextField(max_length=100)

    def __str__(self):
        return self.value

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

    