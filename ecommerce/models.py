from django.db import models
from django.contrib.auth.models import User

# Each class is its own table in database
class Product(models.Model):
	name = models.CharField(max_length=200, null=True)
	description=models.CharField(max_length=200, null=True)
	image=models.ImageField(upload_to='ecommerce/images', null=True) #directory where the image will be stored

	# create Str method
	def __str__(self):
		return self.name

class CartItem(models.Model):
	name = models.CharField(max_length=200, null=True)
	quantity = models.IntegerField(default=1)
	price = models.DecimalField(max_digits=8, decimal_places=2)

	def __str__(self):
		return self.name