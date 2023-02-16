from django.shortcuts import render
# from django.http import HttpResponse
from .models import Product

# Create dummy data which is a list of dictionaries
# products = [
# 	{
# 		'name': 'Dog Toys for Aggressive Chewers',
# 		'description': 'Indestructible Tough Dog Toys for Large Dogs, Durable Squeaky Dog Chew Toys for Small Medium Dog Teeth Cleaning with Natural Rubber',
# 		'image': 'dog_chewer.jpg',
# 	},
# 	{
# 		'name': 'Dog Treat Dispenser',
# 		'description': 'Provide mental stimulation, reduce excessive barking, calm nervous & over-excited dogs, keeps dogs occupied, slow down fast eaters, and soothe gums of teething puppies.',
# 		'image': 'dog_treat_dispenser.jpg',
# 	}
# ]


# Create a function "home" to handle the traffic from homepage of website
# logic for how we want to handle when a user goes to our homepage
def home(request):

	context = {
		'products': Product.objects.all() # keyname

	}
	# render function still return httpresponse in the backgroud
	return render(request, 'ecommerce/home.html', context)
	

def about(request):
	return render(request, 'ecommerce/about.html', {'title': 'About'})

def shoppingcart(request):
	context = {
		'products': Product.objects.all()

	}
	return render(request, 'ecommerce/shoppingcart.html', context)

def productdetails(request):
	context = {
		'products': Product.objects.all()

	}
	return render(request, 'ecommerce/productdetails.html', context)


