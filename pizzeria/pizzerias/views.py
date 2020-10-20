from django.shortcuts import render

# Create your views here.

def index(request):
	""" Pizzeria request. """
	return render(request, 'pizzerias/index.html')