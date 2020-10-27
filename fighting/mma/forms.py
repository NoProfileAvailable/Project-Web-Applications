from django import forms

from .models import Mixedmartialart, Entry

class MixedmartialartForm(forms.ModelForm):
	class Meta:
		model = Mixedmartialart
		fields = ['text']
		labels = {'text': ''}

class EntryForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields = ['text']
		labels = {'text': 'Entry:'}
		widgets = {'text': forms.Textarea(attrs={'cols': 80})}