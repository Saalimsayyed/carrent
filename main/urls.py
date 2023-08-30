from django.contrib import admin
from django.urls import path
from .views import *
from django.conf.urls.static import static
from carbook import settings

app_name = "main"

urlpatterns = [
    path('about', about_view, name='about'),
    path('blog-single', blog_single_view, name='blog-single'),
    path('blog', blog_view, name='blog'),
    path('book/<str:slug>', book_view, name='book'),
    path('car', car_view, name='car'),
    path('car_detail/<str:slug>', car_detail, name='car_detail'),
    path('contact', contact_view, name='contact'),
    path('', index_view, name='index'),
    path('login', login_view, name='login'),
    path('pricing', pricing_view, name='pricing'),
    path('registration', registration_view, name='registration'),
    path('pay', pay_view, name='pay'),
    path('services', services_view, name='services'),
    path('success', success_view, name='success'),
    path('logout', logout_view, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
