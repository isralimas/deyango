# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
import datetime

def suma(request,opera,num1,num2):
	if opera == 'suma':
		now = int(num1) + int(num2)
	elif opera == 'resta' :
		now = int(num1) - int(num2)
	elif opera == 'multiplica' :
		now = int(num1) * int(num2)
	elif opera == 'divide' :
		try :
			now = int(num1) / int(num2)
		except Exception, e :
			now = str(e)
	else :
		now = 'No entendí que clase de operacion quieres hacer'
		#now = datetime.datetime.now()
    #now = datetime.datetime.now()
	html = "<html><body>Isras, el resultado de tu operación es %s.</body></html>" % now
	return HttpResponse(html)

def current_datetime(request,num1,num2):
    #now = int(num1) + int(num2)
    now = datetime.datetime.now()
    html = "<html><body>La hora que marca el reloj es %s.</body></html>" % now
    return HttpResponse(html)