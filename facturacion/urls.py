from django.conf.urls import url
from . import views 


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^categorias/$', views.categorias, name='categorias'),
	url(r'^eliminar-categoria/(?P<idc>\d+)$', views.eliminar_categoria, name='eliminar_categoria'),
	url(r'^insertar-categoria/$', views.insertar_categoria, name='insertar_categoria'),
	url(r'^proveedores/$', views.proveedores, name='proveedores'),
	url(r'^insertar-proveedor/$', views.insertar_proveedor, name='insertar_proveedor'),
]