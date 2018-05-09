from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
# authentication related stuff lives here
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from django.utils.decorators import method_decorator
from .forms import *
from .models import SignUp,Contact1,Comments1,Donate1

class Index(TemplateView):
    
    template_name = 'index.html'

class About(TemplateView):
    
    template_name = 'about.html'

class Blog(TemplateView):
    
    template_name = 'blog.html'

class Children(TemplateView):
    
    template_name = 'children.html'

class Contact(TemplateView):
    
    template_name = 'contact.html'

    def get_context_data(self):
        obj = super().get_context_data()
        obj['contactus'] = ContactUs()
        return obj

   
    
    def post(self, request):

        form = ContactUs(request.POST)
        if form.is_valid():
            Contact1.objects.create(
            name = form.cleaned_data['name'],
         
            email = form.cleaned_data['email'],
            
            url = form.cleaned_data['url'],
            subject = form.cleaned_data['subject'],
            message = form.cleaned_data['message'],
            
                    )
            

            # go to success url
            return HttpResponseRedirect('/')

    # common to both get and post
        context = {
        'form' : form
            }
        return render(request,'/index.html', context)

class Don(TemplateView):
    
    template_name = 'DonateNow.html'

    def get_context_data(self):
        obj = super().get_context_data()
        obj['donate'] = ProductForm()
        return obj

   
    
    def post(self, request):

        form = ProductForm(request.POST)
        if form.is_valid():
            Donate1.objects.create(
            Fname = form.cleaned_data['Fname'],
            Lname = form.cleaned_data['Lname'],
            email = form.cleaned_data['email'],
            phone = form.cleaned_data['phone'],
            street = form.cleaned_data['street'],
            aadhar = form.cleaned_data['aadhar'],
            state = form.cleaned_data['state'],
            pincode = form.cleaned_data['pincode'],
            city = form.cleaned_data['city'],
            dp = form.cleaned_data['dp'],
            donationtype = form.cleaned_data['donationtype'],
            donationamount = form.cleaned_data['donationamount'],
            describe = form.cleaned_data['describe'],
            
                    )
            

            # go to success url
            return HttpResponseRedirect('/')

    # common to both get and post
        context = {
        'form' : form
            }
        return render(request,'/zp/index.html', context)


class Education(TemplateView):
    
    template_name = 'education.html'                        

class Health(TemplateView):
    
    template_name = 'health.html'

class HowCanDonate(TemplateView):
    
    template_name = 'HowCanDonate.html'



class SignUp1(TemplateView):
    
    template_name = 'signup_page.html'
    

    def get_context_data(self):
        obj = super().get_context_data()
        obj['signupform'] = SignUpForm()
        return obj

    def get_queryset(self):
        return SignUp.objects.all()
   
    
    def post(self, request):

        form = SignUpForm(request.POST)
        if form.is_valid():
            SignUp.objects.create(
            username = form.cleaned_data['username'],
            lastname = form.cleaned_data['lastname'],
            email = form.cleaned_data['email'],
            phonenumber = form.cleaned_data['phonenumber'],
            address = form.cleaned_data['address'],
            city = form.cleaned_data['city'],
            state = form.cleaned_data['state'],
            password = form.cleaned_data['password'],
            confirmpassword = form.cleaned_data['confirmpassword']
                    )
            

            # go to success url
            return HttpResponseRedirect('/signin')

    # common to both get and post
        context = {
        'form' : form
            }
        return render(request,'zp/signin.html', context)

    

class SignIn(TemplateView):
    template_name = 'sign_in.html'
    def get_context_data(self):
        obj = super().get_context_data()
        obj['loginForm'] = LoginForm()
        return obj

    @method_decorator(login_required) # we can use multiple decorators here
    def dispatch(self, request):
        return super().dispatch(request)
 

def login_view(request):
    login_error = ""

    if request.user.is_authenticated:
        return HttpResponseRedirect('/')

    if request.method == "GET":
        loginForm = LoginForm()
    elif request.method == "POST":
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            username = loginForm.cleaned_data['username']
            password = loginForm.cleaned_data['password']

            # authenticate here
            user = authenticate(username = username, password = password)

            if user is not None:
                # user authenticated
                login(request, user)
                try:
                    next_page = request.GET['next']
                    return HttpResponseRedirect(next_page)
                except:
                    return HttpResponseRedirect('/')
            else:
                # wrong credentials
                login_error = "Username/Password incorrect"
    
    context = {
    'loginForm' : loginForm,
    'login_error' : login_error
    }
    
    return render(request, 'sign_in.html', context)   

class Single(TemplateView):
    
    template_name = 'single.html'

    def get_context_data(self):
        obj = super().get_context_data()
        obj['comments'] = Comments()
        return obj

   
    
    def post(self, request):

        form = Comments(request.POST)
        if form.is_valid():
            Comments1.objects.create(
            name = form.cleaned_data['name'],
         
            email = form.cleaned_data['email'],
            
            website = form.cleaned_data['website'],
            
            comment = form.cleaned_data['comment'],
            
                    )
            

            # go to success url
            return HttpResponseRedirect('/')

    # common to both get and post
        context = {
        'form' : form
            }
        return render(request,'zp/index.html', context)

class Single1(TemplateView):
    
    template_name = 'single1.html'

class Single2(TemplateView):
    
    template_name = 'single2.html'

class Slider(TemplateView):
    
    template_name = 'slider.html'

class WayToDonate(TemplateView):
    
    template_name = 'WayToDonate.html'

class WhatCanDonate(TemplateView):
    
    template_name = 'WhatCanDonate.html'

class WhoCanDonate(TemplateView):
    
    template_name = 'WhoCanDonate.html'                        
