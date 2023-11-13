from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from datetime import datetime
# Create your views here.
def index(request):
    return render(request, "index.html")

def homepage(request):
    return render(request, "homepage.html")

def loginn(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user=auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('homepage')
        else:
            messages.info(request, "invalid login")
            return redirect('login')
         
    return render(request, "login.html")

def signup(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['phone']
        dob_str = request.POST['dob']
        dob = datetime.strptime(dob_str, "%Y-%m-%d")
        role = request.POST['role']
        password = request.POST['password']
        

        # Validate the inputs
        if not fname or not lname or not email or not phone or not dob or not role or not password:
            messages.info(request, "All fields are required")
            return redirect('signup')
        elif User.objects.filter(email=email).exists():
            messages.info(request, "Email already exists")
            return redirect('signup')
      
        user = User( email=email, password=password)
        user.save()
        messages.success(request, "Registration successful. Please login.")
        return redirect('login')
    
    return render(request, "signup.html")
