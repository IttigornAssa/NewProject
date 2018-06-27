from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Person
from django.forms import ModelForm, TextInput

# from uploads.core.models import Person

class PersonForm(ModelForm):
	abstract = forms.CharField(widget=forms.Textarea(attrs={'rows':10, 'cols':25}))

	
	# document = forms.CharField(widget=forms.Textarea(attrs={'rows':0, 'cols':0}))
	class Meta:
		model =  Person
		exclude=[]
		# abstract = forms.CharField(widget=forms.Textarea),
		# fields = ['name', 'image', 'department','phone_number','document']
        # widgets = {
        #     'name': TextInput(attrs={'class': 'form-control'}),
        #     'image': TextInput(attrs={'class': "form-control"}),
        #     'department': TextInput(attrs={'class': 'form-control'}),           
		# 	'phone_number': TextInput(attrs={'class': 'form-control'}),
        #     'document': TextInput(attrs={'class': "form-control"})
        # }

		# fields = ( 'document', )

	def __init__(self, *args, **kwargs):
		super(PersonForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.add_input(Submit('submit', 'Submit'))
	
