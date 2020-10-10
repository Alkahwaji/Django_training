from django.contrib import admin
from django.urls import path
from . import views

#media libraries
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	path('home/',views.home, name='home'),
	path('login/',views.login, name='login'),
	path('signup/',views.signupuser, name='signup'),
	path('base/',views.base, name='base'),
	path('home/<str:Last_name>/',views.show_data,name = 'show_data'),

]