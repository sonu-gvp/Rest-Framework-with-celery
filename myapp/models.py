from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Register(models.Model):
	"""docstring for Register"""
	first_name = models.CharField(max_length=100, blank=True, default='')
	last_name = models.CharField(max_length=100, blank=True, default='')
	email = models.CharField(max_length=100, blank=True, default='')
	mobile = models.CharField(max_length=15, blank=True, default='')
	image = models.ImageField(upload_to='images/')


class TaskDetails(models.Model):
	"""docstring for TaskDetails"""
	task_id = models.CharField(max_length=100)	
	user_task = models.ForeignKey(User, on_delete=models.CASCADE)
