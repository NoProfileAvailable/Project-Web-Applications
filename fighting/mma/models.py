from django.db import models

# Create your models here.
class Mixedmartialart(models.Model):
	""" Class about the user learns about. """
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		""" Retunr a string representation of the model."""
		return self.text

class Entry(models.Model):
	""" Something specific learned about a topic. """
	topic = models.ForeignKey(Mixedmartialart, on_delete=models.CASCADE)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'entries'

	def __str__(self):
		""" Retunr a string representation of the model."""
		return f"{self.text[:50]}..."