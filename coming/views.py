from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, TemplateView
# Create your views here.

def coming(request):
    return render(request, 'coming_soon.html')

def subscribe(request):
    email = request.POST.get('email')
    send_mail(
        "Thank You",
        "Dear visitor; thank you for subscribing. We will notify you when we go live.", 
        'zamanehsani@outlook.com', 
        [email] , 
        fail_silently=False
        )
    messages.success(request, 'Thank you for subscribing.')
    return redirect('coming_soon')

class Main(ListView):
    template_name = 'main.html'
    model = User

class Landing(TemplateView):
    template_name = 'landing.html'
    