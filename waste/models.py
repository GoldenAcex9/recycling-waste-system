from django.db import models
from django.contrib.auth.models import User

class WasteItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='waste_images/')
    is_recycle = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.description[:20]}"
