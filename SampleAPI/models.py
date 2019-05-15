from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

from uuid import uuid4

def user_image_directory_path(instance, filename):
    return 'user_{0}/image/{1}'.format(instance.user.id, filename)

class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
	message = models.CharField(max_length=150)
	# image = models.ImageField(null=True, blank=True, upload_to=user_image_directory_path)

	def __unicode__(self):
		return "Post: {0}".format(self.user.username)

	def __str__(self):
		return "Post: {0}".format(self.user.username)