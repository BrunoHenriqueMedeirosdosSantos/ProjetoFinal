from django.shortcuts import render
from django.http import HttpResponse
from VirtualMoney import *
# Create your views here.

def index(request):
    context = {}
    return render(request, 'VirtualMoney/index.html', context)
