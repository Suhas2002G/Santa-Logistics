from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def home(request):
    return render(request,'home.html')

def user_login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')



def dashboard(request):
    return render(request,'dashboard.html')