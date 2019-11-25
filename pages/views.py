from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    user = request.user
    return render(request,'home.html',{user: user})
    
def contact_view(request, *args, **kwargs):
    return HttpResponse('<h1>Contact Page</h1>')