from django.conf.urls import url
from . import views 


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^categorias/$', views.categorias, name='categorias'),
	url(r'^insertar-categoria/$', views.insertar_categoria, name='insertar_categoria'),
	url(r'^eliminar-categoria/(?P<idc>\d+)$', views.eliminar_categoria, name='eliminar_categoria'),
	url(r'^actualizar-categoria/(?P<idc>\d+)$', views.actualizar_categoria, name='actualizar_categoria'),

	url(r'^proveedores/$', views.proveedores, name='proveedores'),
	url(r'^insertar-proveedor/$', views.insertar_proveedor, name='insertar_proveedor'),
	url(r'^actualizar-proveedor/(?P<idp>\d+)$', views.actualizar_proveedor, name='actualizar_proveedor'),
	url(r'^eliminar-proveedor/(?P<idp>\d+)$', views.eliminar_proveedor, name='eliminar_proveedor'),

	url(r'^clientes/$', views.clientes, name='clientes'),
	url(r'^insertar-cliente/$', views.insertar_cliente, name='insertar_cliente'),
	url(r'^actualizar-cliente/(?P<idc>\d+)$', views.actualizar_cliente, name='actualizar_cliente'),
	url(r'^eliminar-cliente/(?P<idc>\d+)$', views.eliminar_cliente, name='eliminar_cliente'),
]