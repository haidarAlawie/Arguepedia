from django import forms
from .models import ArgumentPost, Action


class ArgumentPostModelForm(forms.ModelForm):
	class Meta:
		model = ArgumentPost
		fields = [
		'argument_type',
		'title',

		]
class ActionForm(forms.ModelForm):
	class Meta:
		model = Action
		fields = [
		'situation',
		'action',
		'goal',
		'value',
		'explanation'
		]

	#validation to make sure no identical title names
	def clean_title(self, *args, **kwargs ):
		instance = self.instance
		title = self.cleaned_data.get('title')
		qs = ArgumentPost.objects.filter(title__iexact=title)
		if instance is not None:
			qs = qs.exclude(pk=instance.pk)
		if qs.exists():
			raise forms.ValidationError("This title exists already")
		return title