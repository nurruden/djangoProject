from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    #return render(request,content_type="plain/text",context="tttt")
    return HttpResponse('<html><title>To-Do lists</title></html>')