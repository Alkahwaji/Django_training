from django import forms
from .models import signup

class user_form(forms.ModelForm):
	class Meta:
		model = signup
		fields = ['First_name', 'Last_name', 'age', 'email', 'job', 'image' ]

	'''  -------Other way to create forms --------- 
	user_form(forms.Form)
	First_name = forms.CharField()
	Last_name = forms.CharField()
	age = forms.IntegerField()
	email = forms.EmailField()
	job = forms.CharField()
	image = forms.ImageField()
	'''