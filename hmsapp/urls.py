from django.urls import path
from . import views

app_name= 'hmsapp'

urlpatterns=[
    path('', views.home,name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('contact-gv/', views.ContactCreateView.as_view(), name="contact-gv"),
]