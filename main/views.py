from django.shortcuts import render, redirect
from .models import Trip, Carlist, Contact
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import json

def about_view(request):
    return render(request, "main/about.html")

def blog_single_view(request):
    return render(request, "main/blog-single.html")

def blog_view(request):
    return render(request, "main/blog.html")

@login_required(login_url='/login')
def book_view(request, slug):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        email = request.POST['email']
        pick_up = request.POST['pick_up']
        drop_off = request.POST['drop_off']
        pick_date = request.POST['pick_date']
        drop_date = request.POST['drop_date']
        time_pick = request.POST['time_pick']
        print(slug)
        car = Carlist.objects.get(slug=slug)

        trip = Trip(
            first_name=first_name, 
            last_name=last_name, 
            phone=phone, email=email, 
            pick_up=pick_up, 
            drop_off=drop_off, 
            pick_date=pick_date, 
            drop_date=drop_date, 
            time_pick=time_pick,
            car=car
            )
        trip.save()

        context = {
            'status': True,
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email,
        }

        with open("main/static/main/keys.json") as f:
            keys = json.load(f)

        context['key_id'] = keys['key_id']
        context['key_secret'] = keys['key_secret']

        return render(request, 'main/book.html', context)
    else:
        return render(request, 'main/book.html', {"slug":slug})

@login_required(login_url='/login')
def car_single_view(request):
    return render(request, "main/car-single.html")

@login_required(login_url='/login')
def car_view(request):
    cars = Carlist.objects.all()
    return render(request, 'main/car.html', context={'cars': cars})

@login_required(login_url='/login')
def car_detail(request, slug):
    car = Carlist.objects.get(slug=slug)
    context = {}
    context['car'] = car
    return render(request, 'main/car_detail.html', context)

def contact_view(request):
    if request.method == 'POST':
        contact = Contact()
        name=request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.message = message
        contact.save()
        return HttpResponse("Thank For Contacts")
    return render(request, 'main/contact.html')

def index_view(request):
    return render(request, "main/index.html")

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        username = email.split('@')[0]
        next_url = request.POST.get('next', None)

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            if next_url:
                return redirect(next_url)
            else:
                return redirect('/')
        else:
            return redirect('/login')
    else:
        context = {}
        if 'next' in request.GET:
            context['next'] = request.GET['next']
        return render(request, "main/login.html", context)

def pricing_view(request):
    return render(request, "main/pricing.html")

def registration_view(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        username = email.split('@')[0]
    
        user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
        user.save()
        return redirect('/login')
    else:
        return render(request, "main/registration.html")

@login_required(login_url='/login')
def pay_view(request):
    return render(request, "main/pay.html")

def services_view(request):
    return render(request, "main/services.html")

@login_required(login_url='/login')
def success_view(request):
    return render(request, "main/success.html")

def logout_view(request):
    logout(request)
    return redirect('/login')

