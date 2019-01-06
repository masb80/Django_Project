from django.shortcuts import render
from django.http import HttpResponse
#importing loading from django template 
from django.template import loader

# Create your views here.

def index(request):
 #   return HttpResponse('<h3>Byos Securites</h3>')
#def welcome(request):
 #   return HttpResponse('<h3>Welcome to Byos Securites</h3>')
 #getting our template 
    template = loader.get_template('index.html')

    #creating the values to pass
    sendingName = {
        'cname':'Matias',
        'sname':'Samad',
        'ename':'Jiye',
        'mname':'Guido',
        'maname':'Maria',
    }
 
    #rendering the template in HttpResponse
    #but this time passing the context and request
    return HttpResponse(template.render(sendingName, request))
    
    #rendering the template in HttpResponse
   # return HttpResponse(template.render())
