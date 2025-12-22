from django.db import models


class Student(models.Model):
	fullname = models.CharField(max_length=255)
	age = models.IntegerField()
	email = models.EmailField()
	college = models.CharField(max_length=255)
	major = models.CharField(max_length=255)
	year = models.IntegerField()
	info = models.TextField()

	def __str__(self):
		return self.fullname