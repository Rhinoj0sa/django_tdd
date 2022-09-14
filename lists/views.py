from django.http import HttpResponse
from django.shortcuts import render

text = "<html><title>To-Do lists</title><body><p>Are you sure you want to do this?</p></body></html>"


def home_page(request):
    return render(request, 'home.html')
    # return HttpResponse(text)
# Create your views here.
