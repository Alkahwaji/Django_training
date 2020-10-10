from django import forms

class user_form(forms.Form):
	First_name = forms.CharField()
	Last_name = forms.CharField()
	age = forms.IntegerField()
	email = forms.EmailField()
	job = forms.CharField()
	image = forms.ImageField()