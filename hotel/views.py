from django.shortcuts import get_object_or_404, render
from hotel.models import zimmer, buchung
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from django.shortcuts import render_to_response



#from django.forms import 
import datetime

#def zimmerse(request):
#	zeilen = []
#	for m in zimmer.objects.all():
#		zeilen.append("Zimmer: '{}' : Preis: '{}' Euro : Status : '{}'".format(m.zimmer, m.preis, m.status))
#	antwort = HttpResponse('\n'.join(zeilen))
#	antwort['Content-Type'] = 'Text/Plain'
#	return antwort 
	#return render(request, '/home/dgeue/projekte/news_seite/templates/zimmer_list.html', antwort)

def  zimmerse(request):
        template = loader.get_template('zimmer.html')
        context = RequestContext(request,{'zimmer' : zimmer.objects.all()})
        return HttpResponse(template.render(context))

def  buchungen(request):
        template = loader.get_template('buchungen.html')
        context = RequestContext(request,{'buchung' : buchung.objects.all()})
	
        return HttpResponse(template.render(context))

def impressum(request):
   return render_to_response('impressum.html')

def startseite(request):
   return render_to_response('startseite.html')
