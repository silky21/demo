from django.urls import path

from . import views

urlpatterns = [
path('', views.Index.as_view(), name='index'),
path('about/', views.About.as_view(), name='about'),
path('blog/', views.Blog.as_view(), name='blog'),
path('children/', views.Children.as_view(), name='children'),
path('contact/', views.Contact.as_view(), name='contact'),
path('donatenow/', views.Don.as_view(), name='donatenow'),
path('education/', views.Education.as_view(), name='education'),
path('health/', views.Health.as_view(), name='health'),
path('howcandonate/', views.HowCanDonate.as_view(), name='howcandonate'),
path('signin/', views.SignIn.as_view(), name='signin'),
path('login/', views.login_view, name = 'login'),
path('signup/', views.SignUp1.as_view(), name='signup'),
path('single/', views.Single.as_view(), name='single'),
path('single1/', views.Single1.as_view(), name='single1'),
path('single2/', views.Single2.as_view(), name='single2'),
path('slider/', views.Slider.as_view(), name='slider'),
path('waytodonate/', views.WayToDonate.as_view(), name='waytodonate'),
path('whatcandonate/', views.WhatCanDonate.as_view(), name='whatcandonate'),
path('whocandonate/', views.WhoCanDonate.as_view(), name='whocandonate'),
              
]
    