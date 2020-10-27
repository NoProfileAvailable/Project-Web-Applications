from django.db import models

class Pizza(models.Model):
	""" Some pizza"""
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		""" Return a string representation of the Model. """
		return self.text

class Toppings(models.Model):
	""" Toppings for the pizzas. """
	topping = models.ForeignKey(Pizza, on_delete=models.CASCADE)
	text = models.TextField()
	date_added= models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'entries'

	def __str__(self):
		""" Return the representation of the model."""
		return f"{self.text[:50]}..."