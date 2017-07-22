from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User

@python_2_unicode_compatible
class Categoria(models.Model):
	nombre = models.CharField(max_length=50)

	def __str__(self):
		return self.nombre 

@python_2_unicode_compatible
class Proveedor(models.Model):
	rtnProveedor = models.CharField(max_length=16)
	nombreContacto = models.CharField(max_length=70)
	nombreEmpresa = models.CharField(max_length=50)
	correoContacto = models.CharField(max_length=70)
	direccion = models.TextField()
	telefonoContacto = models.CharField(max_length=9,null=True, blank=True)
	telefonoEmpresa = models.CharField(max_length=9,null=True, blank=True)

	def __str__(self):
		return self.nombreEmpresa

@python_2_unicode_compatible
class Producto(models.Model):
	nombre = models.CharField(max_length=50)
	stockMinimo = models.IntegerField()
	existencia = models.IntegerField()
	precioCosto = models.DecimalField(max_digits=7, decimal_places=2)
	precioVenta = models.DecimalField(max_digits=7, decimal_places=2)
	proveedor = models.ForeignKey(Proveedor)
	categoria = models.ForeignKey(Categoria)

	def __str__(self):
		return self.nombre 

@python_2_unicode_compatible
class Cliente(models.Model):
	rtn = models.CharField(max_length=16, null=True, blank=True)
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	correo = models.CharField(max_length=50)
	direccion = models.TextField()
	telefono = models.CharField(max_length=9,null=True, blank=True)

	def __str__(self):
		return self.nombre 

@python_2_unicode_compatible
class Factura(models.Model):
	fecha = models.DateField(auto_now=True)
	cliente = models.ForeignKey(Cliente)

	def __str__(self):
		return unicode(self.id)

@python_2_unicode_compatible
class DetalleFactura(models.Model):
	producto = models.ForeignKey(Producto)
	factura = models.ForeignKey(Factura)
	cantidad = models.IntegerField()
	precio = models.DecimalField(max_digits=7, decimal_places=2)

	def __str__(self):
		return unicode(self.id) 


