from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    my_context = {
        'my_text': 'Hello World',
        'my_list': [10,20,30,'a']
    }
    return render(request,'home.html',my_context)
    
def contact_view(request, *args, **kwargs):
    return render(request,'contact.html',{})
    
def about_view(request, *args, **kwargs):
    return HttpResponse('<h1>About Page</h1>')