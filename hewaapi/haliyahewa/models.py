from django.db import models

class Haliyahewa(models.Model):
	mkoa = models.CharField(max_length=200)
	mvua = models.CharField(max_length=10)
	nyuzi = models.CharField(max_length=10)

	def __str__(self):
		return self.mkoa