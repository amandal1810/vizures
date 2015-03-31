from django.conf.urls import patterns, url
from rat import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^process/', views.process, name='process'),
    )