from django.shortcuts import render,redirect
from .models import Form


def form(request):
    
    if request.method=='POST':
        a=request.POST.get('username')
        b=request.POST.get('firstname')
        c=request.POST.get('lastname')
        d=request.POST.get('email')
        e=request.POST.get('password')
    
        formuser=Form(username=a,firstname=b,lastname=c,email=d,password=e)
        formuser.save();
        return redirect('/')
    else:
        return render(request,'index.html')
