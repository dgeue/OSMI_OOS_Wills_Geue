from django.conf.urls import url, include, patterns
from . import views

urlpatterns = patterns('',
    #url(r'^$', views.buchungen),
    #url(r'^$', views.zimmerse),
    #url(r'^zimmerse/', views.zimmerse),
    url(r'^$', views.zimmerse, name='zimmer'),
    url(r'buchungen/$', views.buchungen, name='buchung'),
    #url(r'^test/$', views.test, name='test'),

)
