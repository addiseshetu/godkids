from django.shortcuts import render, get_object_or_404
from django.http import Http404 
from .models import Kid

def index(request):
    context = {
        "kids":Kid.objects.all()
        
    }
    return render(request, 'godkids/index.html', context)

def detail(request, security_code):
    context = {
        "kids": Kid.objects.get(pk=security_code)

    }
    return render(request, 'godkids/detail.html', context)

