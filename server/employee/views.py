from django.shortcuts import render
from .models import Employee
# Create your views here.

def LoginView(request):
    context={}
    if(request.method=="POST"):
        queryset=Employee.objects.all()
        if request.POST.get('username') and request.POST.get('pwd') in queryset:
            print("Login successfull!")
            context = {"error": "Login successfull"}
        else:
            print("Login unsuccessfull!")
            context ={"error":"Login unsuccessfull"}
    return render(request,"login.html",context)

# def RegisterView(request):
#     return render(request,"reg.html",{})
def RegisterView(request):
    if (request.method=="POST"):
        fname =request.POST.get('fname')
        lname =request.POST.get('lname')
        email =request.POST.get('email')
        contact =request.POST.get('contact')
        username =request.POST.get('username')
        pwd =request.POST.get('pwd')
        dob =request.POST.get('dob')
        bio =request.POST.get('bio')
        jobrole =request.POST.get('jobrole')
        Employee.objects.create(fname=fname,lname=lname,email=email,contact=contact,username=username,pwd=pwd,dob=dob,bio=bio,jobrole=jobrole)
    return render(request,"reg.html",{})