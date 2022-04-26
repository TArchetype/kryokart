from django.shortcuts import render
from django.core import serializers
from .models import GPS
from django.http import JsonResponse, HttpResponse
from .forms import GPSForm

def index(request):
    return render(request, 'upload.html')

def jsonGPS(request):
    objects = list(GPS.objects.values())

    return JsonResponse(objects, safe=False)

def hook(request):
    if request.method == 'post':
        data = request.data
        form = GPSForm(request.post)
        if(form.is_valid()):
            form.save()
            return HttpResponse()
    def post(self, request, *args, **kwargs):
        
        return HttpResponse()
