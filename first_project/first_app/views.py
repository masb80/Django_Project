from django.shortcuts import render
from django.http import HttpResponse
#importing loading from django template 
from django.template import loader
from first_app.models import Topic, AccessRecord, Webpage


from first_app import forms 
import wifi
from wifi import Cell, Scheme

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
    #return HttpResp   onse(template.render(sendingName, request))
    webpage_lists = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpage_lists}

    #return render(request, 'index.html', context=date_dict)


    return render(request, 'first_app/index.html', context=date_dict) 

def form_name_view(request):   
    form = forms.formName()

    if request.method == 'POST':
        form = forms.formName(request.POST)
        print("SSID is: " + request.POST['ssid'])
        print("Password is: " + request.POST['password'])  
        ssid =  request.POST['ssid']
        password = request.POST['password']    
        ConnectWiFi(ssid, password)    
        print("Connected to the network", ssid)                

    if form.is_valid():
        print('VALIDATION SUCCESS !')
        print("SSID is" + form.cleaned_data['SSID'])
        print("Password is" + form.cleaned_data['Password'])

    return render(request, 'first_app/form_page.html', {'form':form})

def Search():
    wifilist = []
    cells = wifi.Cell.all('wlan0')
    for cell in cells:
        wifilist.append(cell)
    return wifilist

def FindFromSearchList(ssid):
    wifilist = Search()
    for cell in wifilist:
        dssid = str(cell.ssid).split("\"")[0]
        cell.ssid = dssid
	#print("*******************"+dssid+"*********************************")
        if cell.ssid == ssid:
            return cell
    return False

def ConnectWiFi(ssid, passwd): 
    print("**ssid  ", ssid)
    print("**Password  ", passwd)
    '''
    cell = wifi.Scheme.find('wlan0', ssid)
    if cell:
        scheme = Scheme.for_cell('wlan0',ssid,cell, passwd)
        scheme.activate()
    else:
	    cell = FindFromSearchList(ssid)
	    scheme = Scheme.for_cell('wlan0',ssid,cell, passwd)
	#mystring=str(scheme)
	#print("*******************"+mystring+"*********************************")
    if cell:
	    scheme.save()
	    scheme.activate() 
        '''
    return True      
       
   
    
    #rendering the template in HttpResponse
   # return HttpResponse(template.render())
