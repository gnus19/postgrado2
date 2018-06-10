# -*- coding: utf-8 -*-


from . import views
from django.conf.urls import url
from django.contrib.auth.views import login, logout


app_name = 'coordinaAsignaturas'
urlpatterns = [
	url(r'^$', views.home),
	url(r'^login/$', views.home),
	url(r'^logout/$', login, {'template_name': 'coordinaAsignaturas/logout.html'}),
	url(r'^ver/$', views.vistaAsignaturas, name='verAsignaturas'),
	#url(r'^agregar/', views.agregarAsignatura),
	#url(r'^editar/', views.editarAsignatura),
	url(r'^modificar/(?P<codAsig>[-\w]+)/$', views.modificarAsignatura, name='modificarAsignatura'),
	url(r'^agregar/$', views.agregarAsignatura, name='agregarAsignatura'),
	url(r'^detalles/$', views.detallesAsignatura, name='detallesAsignatura'),
	url(r'^principal/$', views.principal, name='principal'),
	url(r'^(?P<id>\d+)/$', views.vistaOfertas, name='oferta')
]