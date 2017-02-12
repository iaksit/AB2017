import os

from django.contrib.auth.models import User
from django.db import models

from collectivework.settings import MEDIA_URL


def get_image_path(instance, filename):
    return os.path.join(MEDIA_URL, 'images', str(instance.user.id), filename)


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    city = models.CharField(max_length=45)
    profile_photo = models.ImageField(upload_to=get_image_path, blank=True, null=True)

    def __unicode__(self):
        return self.user.username

    def get_image_relative_path(self):
        return os.path.join('static', 'images', str(self.user.id), self.profile_photo.name)
