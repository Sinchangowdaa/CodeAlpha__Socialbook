from django.db import models
from django.contrib.auth import get_user_model

user = get_user_model()

# Create your models here.
class profile(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegrateField()
    bio = models.Text.Field(blank=True)
    profileimg = models.ImageField(upload_to='profile_images',default='download.jpeg')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username