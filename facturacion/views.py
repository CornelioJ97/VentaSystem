from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from .models import Categoria, Proveedor, Cliente
from .forms import CategoriaForm, ProveedorForm, ClienteForm

@login_required()
def index(request):
	return render(request, 'index.html')

@login_required()
def categorias(request):
	categorias = Categoria.objects.all().order_by('id')
	return render(request, 'categoria.html', {'categorias': categorias})

@login_required()
def insertar_categoria(request):
	if request.method == 'POST':
		form = CategoriaForm(request.POST)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('categorias'))
	else:
		form = CategoriaForm()
	return render(request, 'categoria_form.html', {'form': form})

@login_required()
def actualizar_categoria(request, idc):
	categoria = Categoria.objects.get(id=idc)
	if request.method == 'GET':
		form = CategoriaForm(instance=categoria)
	else:
		form = CategoriaForm(request.POST, instance=categoria)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('categorias'))
	return render(request, 'categoria_form.html', {'form': form})

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
		form = ProveedorForm(request.POST)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('proveedores'))
	else:
		form = ProveedorForm()
	return render(request, 'proveedor_form.html', {'form': form})

@login_required()
def actualizar_proveedor(request, idp):
	proveedor = Proveedor.objects.get(id=idp)
	if request.method == 'GET':
		form =ProveedorForm(instance=proveedor)
	else:
		form = ProveedorForm(request.POST, instance=proveedor)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('proveedores'))
	return render(request, 'proveedor_form.html', {'form': form})

@login_required()
def eliminar_proveedor(request, idp):
	proveedor = Proveedor.objects.get(pk=idp)
	proveedor.delete()
	return HttpResponseRedirect(reverse('proveedores'))




@login_required()
def clientes(request):
	clientes = Cliente.objects.all().order_by('-rtn')
	return render(request, 'cliente.html', {'clientes': clientes})

@login_required()
def insertar_cliente(request):
	if request.method == 'POST':
		form = ClienteForm(request.POST)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('clientes'))
	else:
		form = ClienteForm()
	return render(request, 'cliente_form.html', {'form': form})

@login_required()
def actualizar_cliente(request, idc):
	cliente = Cliente.objects.get(id=idc)
	if request.method == 'GET':
		form =ClienteForm(instance=cliente)
	else:
		form = ClienteForm(request.POST, instance=cliente)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('clientes'))
	return render(request, 'cliente_form.html', {'form': form})

@login_required()
def eliminar_cliente(request, idc):
	cliente = Cliente.objects.get(pk=idc)
	cliente.delete()
	return HttpResponseRedirect(reverse('clientes'))





