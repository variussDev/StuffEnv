from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings 

urlpatterns = [
        url( r'^$', views.home, name="home" ),
        url( r'^settings/$', views.settings, name="Ustawienia" ),
        url( r'^listAll/$', views.showAll, name="listaWszystkie" ),
        url( r'^tests/$', views.devForm, name="tests" ),
        url( r'^(?P<part>[a-z]+)List/$', views.detailedList, name="listaSzczegolowa"),
        url( r'^edit/(?P<id>[0-9]+)/$', views.edit, name="edycja"), 
] + static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
