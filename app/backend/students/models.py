from django.db import models

class Student(models.Model):
	name = models.CharField(max_length=200)
	course = models.CharField(max_length=200)
	rating = models.IntegerField()

	class Meta:
		ordering = ['name']

	def __str__(self):
		return f"{self.name} - {self.course} - {self.rating}"
