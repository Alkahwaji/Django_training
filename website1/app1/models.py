from django.db import models

# Create your models here.

class signup(models.Model):
	class Meta:
		verbose_name_plural  = 'signups'
	First_name = models.CharField(max_length=120)
	Last_name = models.CharField(max_length=120)
	age = models.IntegerField(default=16)
	email = models.EmailField()
	address = models.TextField()
	job = models.CharField(max_length=70)
	image = models.ImageField(upload_to='users/')


	def __str__(self):
		return self.Last_name


