from django.db import models

# Create your models here.
class Note(models.Model):
    body = models.TextField(null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[:50]