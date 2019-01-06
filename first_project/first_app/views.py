from django.shortcuts import render
from django.http import HttpResponse
#importing loading from django template 
from django.template import loader
from first_app.models import Topic, AccessRecord, Webpage

# Create your views here.

def index(request):
 #   return HttpResponse('<h3>Byos Securites</h3>')
#def welcome(request):
 #   return HttpResponse('<h3>Welcome to Byos Securites</h3>')
 #getting our template 
 #   template = loader.get_template('index.html')

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
    #return HttpResponse(template.render(sendingName, request))
    webpage_lists = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpage_lists}

    #return render(request, 'index.html', context=date_dict)
    return render(request, 'first_app/index.html', context=date_dict)

    
    #rendering the template in HttpResponse
   # return HttpResponse(template.render())
