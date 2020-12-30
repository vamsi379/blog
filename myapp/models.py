from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserTimestamp(models.Model):
	user = models.ForeignKey(User,on_delete = models.CASCADE)
	timestamp = models.DateTimeField(auto_now_add = True)

	class Meta:
		abstract = True

class Blog(UserTimestamp):
	title = models.CharField(max_length = 50)
	description = models.TextField()
	img1 = models.ImageField(upload_to = '')
	img2 = models.ImageField(upload_to = '')
	img3 = models.ImageField(upload_to = '')

	def __str__(self):
		return self.title

