from django.shortcuts import render,HttpResponse
from homeapp.models import Contact

# Create your views here.
def home(request):
    return render(request,'home.html')

def contact(request):
    
    if request.method=="POST":
        name,email,phone,desc=request.POST['name'],request.POST['email'],request.POST['phone'],request.POST['desc']
        ins=Contact(name=name,email=email,phone=phone,desc=desc)
        ins.save()
    return render(request,'contact.html')

    