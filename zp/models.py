from django.db import models


# Create your models here.
class SignUp(models.Model):
    username = models.CharField(max_length = 100)
    lastname = models.CharField(max_length = 100)
    email = models.CharField(max_length=200)
    phonenumber = models.CharField(max_length=12)
    address = models.TextField()
    city = models.CharField(max_length = 200)
    state = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)
    confirmpassword = models.CharField(max_length = 200)

class Contact1(models.Model):
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()

class Comments1(models.Model):
    name = models.CharField(max_length = 100,)
    email = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    comment = models.TextField()    

CITY = [
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
    
        
]

TYPE = [
    ('children','Children'),
    ('disabled','Disabled'),
    ('environment','Environment'),
    ('youth','Youth'),
    ('women','Women'),
    ('education','Education'),
    ('health','Health'),
    ('elderly','Elderly'),
    ('food','Food'),
    
        
]

AMOUNT = [
    ('₹500','₹500'),
    ('₹1000','₹1000'),
    ('₹2000','₹2000'),
    ('₹5000','₹5000'),
    ('₹10,000','₹10,000'),
    ('₹20,000','₹20,000'),
    ('₹30,000','₹30,000'),
    ('₹40,000','₹40,000'),
    ('₹50,000','₹50,000'),
]    

def upload_image(instance, Fname):
    return 'dp/' + instance.Fname + '/' + Fname

class Donate1(models.Model):
    Fname = models.CharField(max_length = 100)
    Lname = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
 
    phone = models.CharField(max_length=100)
    street = models.CharField(max_length = 100)
    aadhar = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)
    city = models.CharField(max_length = 100,choices=CITY )
    dp = models.ImageField(upload_to=upload_image, null = True)
    donationtype = models.CharField(max_length=200,choices=TYPE)
    donationamount = models.CharField(max_length=200,choices=AMOUNT)
   
    describe = models.TextField()
