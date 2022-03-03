from django.shortcuts import render

from django.shortcuts import render

def index(request):
    print("Dette blir printa i terminalen")
    context = {} # Tom dictionary som blir brukt senere!
    return render(request, "elsysapp/index.html", context)
    
