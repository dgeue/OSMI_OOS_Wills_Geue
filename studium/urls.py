from django.conf.urls import include, url
from django.contrib import admin
from lightbox.views import ImagePageView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls), name='admin'), 
    url(r'^zimmer/$', 'hotel.views.zimmerse', name='zimmer'),
    url(r'^buchungen/$', 'hotel.views.buchungen', name='buchungen'),
    #url('^$',include('hotel.urls', namespace='buchung')),
    url(r'^$', 'hotel.views.zimmerse', name='zimmer'),
    url(r'^impressum/', 'hotel.views.impressum', name='impressum'),
    url(r'^startseite/', 'hotel.views.startseite', name='startseite'),

]
