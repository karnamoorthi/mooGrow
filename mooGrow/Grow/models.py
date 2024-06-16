from django.db import models

# Create your models here.


class join(models.Model):
	Id=models.AutoField(primary_key=True)
	Fullname=models.CharField(max_length=100)
	Mobileno=models.CharField(max_length=100)
	Message=models.CharField(max_length=100)

	class Meta:
		db_table="contact"

class put(models.Model):
	Id=models.AutoField(primary_key=True)
	Fullname=models.CharField(max_length=100)
	Email=models.CharField(max_length=100)
	Company=models.CharField(max_length=100)
	Website=models.CharField(max_length=100)
	Mobileno=models.CharField(max_length=100)
	Message=models.CharField(max_length=100)

	class Meta:
		db_table="login"

class cart(models.Model):
	Id=models.AutoField(primary_key=True)
	Fullname=models.CharField(max_length=100)
	Mobileno=models.CharField(max_length=100)
	Email=models.CharField(max_length=100)
	Company=models.CharField(max_length=100)
	Message=models.CharField(max_length=100)

	class Meta:
		db_table="order"