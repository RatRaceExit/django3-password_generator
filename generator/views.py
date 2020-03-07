from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request,'generator/home.html')
    
def about(request):
    return render(request,'generator/about.html')

def password(request):
    thepassword = ''
    if request.GET.get('length').isdigit():
        length = int(request.GET.get('length',8))
    else:
        length = 8

    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special_characters'):
        characters.extend(list('~!@#$%^&*()_+'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request,'generator/password.html', {'password':thepassword})
