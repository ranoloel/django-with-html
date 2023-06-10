from django.shortcuts import render

# Create your views here.
def homePage(request):
    return render(request, "index.html")

def contactUs(request):
    return render(request, "contact.html")