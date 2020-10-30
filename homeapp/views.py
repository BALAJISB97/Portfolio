from django.shortcuts import render,HttpResponse
from homeapp.models import Contact
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def home(request):
    return render(request,'home.html')

def contact(request):
    
    if request.method=="POST":
        name,email,phone,desc=request.POST['name'],request.POST['email'],request.POST['phone'],request.POST['desc']
        ins=Contact(name=name,email=email,phone=phone,desc=desc)
        ins.save()
        #construct mail message
        msg="Hey Balaji,"+name+" has enquired about you. Please check. Below are the details of the person\n"+"phone number = "+phone+"\nemail: "+email+"\n and his enquiry is "+desc
        print(msg)
        send_to_me(msg)
    return render(request,'contact.html')

def send_to_me(msg):
    send_mail('Contact Form',msg,settings.EMAIL_HOST_USER,['balajisb147@gmail.com'],fail_silently=False)
    return True

    