from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import user_form
from .models import signup


# Create your views here.
def base(request):
	
	return render(request, 'base.html', {})

def home(request):
	return render(request, 'home.html', {})

def login(request):
	return render(request, 'login.html', {})

def signupuser(request):
	form = user_form(request.POST or None)
	model_obj = signup()
	if form.is_valid():
		model_obj.First_name  = form.cleaned_data['First_name']
		model_obj.Last_name = form.cleaned_data['Last_name']
		model_obj.age = form.cleaned_data['age']
		model_obj.email = form.cleaned_data['email']
		model_obj.job  = form.cleaned_data['job']
		model_obj.image = form.cleaned_data['image']
		model_obj.save()
		return HttpResponseRedirect('/signup')
	return render(request,'signup.html',{'form':form})

	 
def show_data(request,Last_name):
	context = {}
	context['data'] = signup.objects.get(Last_name = Last_name)
	return render(request,'home.html',context)
