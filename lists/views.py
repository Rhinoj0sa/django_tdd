from django.http import HttpResponse
from django.shortcuts import render

text = "<html><title>To-Do lists</title><body><p>Are you sure you want to do this?</p></body></html>"


def home_page(request):
    if request.method == 'POST':
        return HttpResponse(request.POST['item_text'])
    return render(request, 'home.html')

