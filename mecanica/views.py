from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def start(request):
    return render (request, 'start.html')