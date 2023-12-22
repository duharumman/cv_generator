import json
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.template import loader

def index(request):
    # Task 4: Add Solution here
    return render(request,"CV_gen/index.html")

def cv_list(request):
    return render(request,"CV_gen/list.html")

def submit(request):
    # Task 7: Add Solution here
    pass

# Task 8: Add Solution here