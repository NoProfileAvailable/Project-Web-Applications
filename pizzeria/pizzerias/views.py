from django.shortcuts import render

from .models import Toppings

def index(request):
	"""The home page for pizzerias. """
	return render(request, 'pizzerias/index.html')

def toppings(request):
	""" Show all toppings. """
	toppings = Toppings.objects.order_by('date_added')
	context = {'toppings': toppings}
	return render(request, 'pizzerias/toppings.html', context)

def topping(request, topping_id):
	""" Show one topping. """
	topping = Toppings.objects.get(id=topping_id)
	entries = topping.entry_set.order_by('date_added')
	context = {'topping': topping, 'entries': entries}
	return render(request, 'pizzerias/topping.html', context)
