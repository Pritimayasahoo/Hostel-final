from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home/home.html')

def activities(request):
    return render(request,'home/Activities.html')

def admission(request):
    return render(request,'home/Admission.html')

def notice(request):
    return render(request,'home/Notice.html')

def profile(request):
    return render(request,'home/profile.html')

def Staffs(request):
    return render(request,'home/staffs.html')