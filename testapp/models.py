from django.db import models
# Create your models here.

class simpleTest(models.Model):
	name = models.CharField(max_length = 20)
	geder = models.CharField(max_length = 20)