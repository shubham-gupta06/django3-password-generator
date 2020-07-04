from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
	return render(request, 'generator/home.html')
def about(request):
	return render(request,'generator/about.html')

def password(request):

	
	characters = list('abcdefghijklmnopqrstuvwxyz')

	if request.GET.get('upper'):
		characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
	if request.GET.get('number'):
		characters.extend(list('0123456789'))
	if  request.GET.get('special'):
		characters.extend(list('!@#$%^&*()'))

    
	length = int(request.GET.get('length', 12))
	thepassword= ''
	for x in range(length):
	 	thepassword+= random.choice(characters)
	return render(request, 'generator/password.html', {'password' : thepassword})

