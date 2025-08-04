from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    biografia = models.TextField(blank=True, null=True)  # Campo extra a elección

    def __str__(self):
        return f"Perfil de {self.user.username}"
