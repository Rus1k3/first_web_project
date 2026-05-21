from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.name


class EmailMessage(models.Model):
    sender = models.CharField(max_length=255)
    recipient = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    received_at = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    null=True,
    blank=True
)
    
    image = models.ImageField(
        upload_to='emails/',
        blank=True,
        null=True
    )

    tags = models.ManyToManyField(
        Tag,
        blank=True
    )

    def __str__(self):
        return self.subject
    