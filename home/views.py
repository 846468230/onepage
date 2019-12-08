from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.template import loader
def helloworld(request):
    return HttpResponse("Helloworld!")

def index(request):
    template = loader.get_template("home/index.html")
    return HttpResponse(template.render({},request))