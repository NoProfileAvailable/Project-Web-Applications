from django.db import models, migrations

# Create your models here.

class Pizza(models.Model):
	""" some pizza things, you know. """
	atomic = False
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		""" Return a string representation of the model."""
		return self.text


class Topping(models.Model):
	""" Marhgarita pizza. """
	pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'entries'

	def __str__(self):
		""" Return a string representation of the model. """

		return self.name

