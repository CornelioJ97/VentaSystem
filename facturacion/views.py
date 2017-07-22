from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from .models import Categoria, Proveedor

@login_required()
def index(request):
	return render(request, 'index.html')

@login_required()
def categorias(request):
	categorias = Categoria.objects.all().order_by('-nombre')
	return render(request, 'categoria.html', {'categorias': categorias})

@login_required()
def insertar_categoria(request):
	if request.method == 'POST':
		nombre = request.POST.get('nombre')
		ct = Categoria(nombre=nombre)
		ct.save()
		return HttpResponseRedirect(reverse('categorias'))

	else:
		return HttpResponse('Hay un error')

@login_required()
def eliminar_categoria(request, idc):
	categoria = Categoria.objects.get(pk=idc)
	categoria.delete()
	return HttpResponseRedirect(reverse('categorias'))

@login_required()
def proveedores(request):
	proveedores = Proveedor.objects.all().order_by('-rtnProveedor')
	return render(request, 'proveedor.html', {'proveedores': proveedores})

@login_required()
def insertar_proveedor(request):
	if request.method == 'POST':
		rtn = request.POST.get('rtnProveedor')
		nombreContacto = request.POST.get('nombreContacto')
		nombreEmpresa = request.POST.get('nombreEmpresa')
		correo = request.POST.get('correo')
		direccion = request.POST.get('direccion')
		telefonoContacto = request.POST.get('telefonoContacto')
		telefonoEmpresa = request.POST.get('telefonoEmpresa')
		ct = Proveedor(rtnProveedor=rtn, nombreContacto = nombreContacto, nombreEmpresa = nombreEmpresa, correoContacto = correo, direccion = direccion, telefonoContacto = telefonoContacto, telefonoEmpresa = telefonoEmpresa)
		ct.save()
		return HttpResponseRedirect(reverse('proveedores'))

	else:
		return HttpResponse('Hay un error')
