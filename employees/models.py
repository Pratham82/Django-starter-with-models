from django.db import models

# Create your models here.
class employees_db(models.Model):
	emp_id = models.AutoField
	firstName = models.CharField(max_length=30)
	lastName = models.CharField(max_length=30)
	dept = models.CharField(max_length=30)
	salary = models.IntegerField()

	def __str__(self):
	 return self.firstName