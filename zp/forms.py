from django import forms
from .models import *

class SignUpForm(forms.Form):
    username = forms.CharField(max_length = 100)
    lastname = forms.CharField(max_length = 100)
    email = forms.CharField(max_length=200)
    phonenumber = forms.CharField(max_length=12)
    address = forms.CharField(widget = forms.Textarea())
    city = forms.CharField(max_length = 200)
    state = forms.CharField(max_length = 200)
    password = forms.CharField(max_length = 200, widget = forms.PasswordInput())
    confirmpassword = forms.CharField(max_length = 200, widget = forms.PasswordInput())

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length = 200 , widget = forms.PasswordInput())

class ContactUs(forms.Form):
    name = forms.CharField(max_length = 100,widget = forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.CharField(max_length=200,widget = forms.TextInput(attrs={'placeholder': 'Email'}))
    url = forms.CharField(max_length=200,widget = forms.TextInput(attrs={'placeholder': 'URL'}))
    subject = forms.CharField(max_length=200,widget = forms.TextInput(attrs={'placeholder': 'Subject'}))
    message = forms.CharField(widget = forms.Textarea(attrs={'placeholder': 'Message'}))

class Comments(forms.Form):
    name = forms.CharField(max_length = 100,widget = forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.CharField(max_length = 100,widget = forms.TextInput(attrs={'placeholder': 'Email'}))
    website = forms.CharField(max_length = 100,widget = forms.TextInput(attrs={'placeholder': 'Website'}))
    comment = forms.CharField(widget = forms.Textarea(attrs={'placeholder': 'Comments'}))



CITY = (
    ('agra','Agra'),
    ('agartala','Agartala'),
    ('bhopal','Bhopal'),
    ('bangalore','Bangalore'),
    ('delhi','Delhi'),
    ('kolkata','Kolkata'),
    ('dehradun','Dehradun'),
    ('lucknow','Lucknow'),
    ('chandigarh','Chandigarh'),
    ('hyderabad','Hyderabad'),
    ('chennai','Channei'),
    ('patna','Patna'),
    
        
)

TYPE = (
    ('children','Children'),
    ('disabled','Disabled'),
    ('environment','Environment'),
    ('youth','Youth'),
    ('women','Women'),
    ('education','Education'),
    ('health','Health'),
    ('elderly','Elderly'),
    ('food','Food'),
    
        
)

AMOUNT = (
    ('₹500','₹500'),
    ('₹1000','₹1000'),
    ('₹2000','₹2000'),
    ('₹5000','₹5000'),
    ('₹10,000','₹10,000'),
    ('₹20,000','₹20,000'),
    ('₹30,000','₹30,000'),
    ('₹40,000','₹40,000'),
    ('₹50,000','₹50,000'),
)

class DonateForm(forms.Form):
    Fname = forms.CharField(max_length = 100,widget = forms.TextInput(attrs={'placeholder': 'First Name'}))
    Lname = forms.CharField(max_length=200,widget = forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email = forms.CharField(max_length=200,widget = forms.TextInput(attrs={'placeholder': 'Email'}))
    phone = forms.CharField(max_length = 100,widget = forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    street = forms.CharField(max_length=200,widget = forms.TextInput(attrs={'placeholder': 'Street Address'}))
    aadhar = forms.CharField(max_length=200,widget = forms.TextInput(attrs={'placeholder': 'Aadhar Number'}))
    state = forms.CharField(max_length=200,widget = forms.TextInput(attrs={'placeholder': 'State'}))
    pincode = forms.CharField(max_length=200,widget = forms.TextInput(attrs={'placeholder': 'Pincode'}))
    city = forms.ChoiceField(choices=CITY),
    donationtype = forms.ChoiceField(choices=TYPE),
    donationamount = forms.ChoiceField(choices=AMOUNT),
    describe = forms.CharField(widget = forms.Textarea(attrs={'placeholder': 'What you want to donate...Describe!!!'}))
    

class ProductForm(forms.ModelForm):
	class Meta:
		model = Donate1
		fields = '__all__'
        
