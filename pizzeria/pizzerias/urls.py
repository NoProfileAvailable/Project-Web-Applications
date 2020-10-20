""" Defines URL patterns for pizzerias. """

from django.urls import path

from . import views
app_name = 'pizzerias'
urlpatterns = [
	# Home Page
	path('', views.index, name='index'),
	# Show all toppings
	path('toppings/', views.toppings, name='toppings'),
	# Detail page for a single topping
	path('toppings/<int:topping_id>/', views.topping, name='topping'),
]