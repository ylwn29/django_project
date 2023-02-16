from django.shortcuts import render, redirect, get_object_or_404
# from django.http import HttpResponse
from .models import Product, CartItem
from .forms import CartItemForm

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


def cart_list(request):
	context = {
		'items': CartItem.objects.all()

	}
	return render(request, 'ecommerce/cart_list.html', context)

def cart_add(request):
    if request.method == 'POST':
        form = CartItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cart_list')
    else:
        form = CartItemForm()
    return render(request, 'ecommerce/cart_form.html', {'form': form})

def cart_update(request, pk):
    item = get_object_or_404(CartItem, pk=pk)
    if request.method == 'POST':
        form = CartItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('cart_list')
    else:
        form = CartItemForm(instance=item)
    return render(request, 'ecommerce/cart_form.html', {'form': form})

def cart_delete(request, pk):
    item = get_object_or_404(CartItem, pk=pk)
    item.delete()
    return redirect('cart_list')



def productdetails(request):
	context = {
		'products': Product.objects.all()

	}
	return render(request, 'ecommerce/productdetails.html', context)


