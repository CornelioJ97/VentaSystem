#coding: utf8
from django import forms
from .models import Categoria, Proveedor, Cliente

class CategoriaForm(forms.ModelForm):

	class Meta:
		model = Categoria

		fields= [
			'nombre',
		]

		labels = {
			'nombre': 'Nombre Categoría',
		}

		widgets = {
			'nombre': forms.TextInput(attrs={'class': 'form-control controles', 'required': 'True'}),
		}

class ProveedorForm(forms.ModelForm):

	class Meta:
		model = Proveedor

		fields= [
			'rtnProveedor',
			'nombreContacto',
			'nombreEmpresa',
			'correoContacto',
			'direccion',
			'telefonoContacto',
			'telefonoEmpresa',
		]

		labels = {
			'rtnProveedor': 'RTN Proveedor',
			'nombreContacto': 'Nombre Contacto',
			'nombreEmpresa': 'Nombre Empresa',
			'correoContacto': 'Correo Contacto',
			'direccion': 'Dirección',
			'telefonoContacto': 'Teléfono Contacto',
			'telefonoEmpresa': 'Teléfono Empresa',

		}

		widgets = {
			'rtnProveedor': forms.TextInput(attrs={'class': 'form-control'}),
			'nombreContacto': forms.TextInput(attrs={'class': 'form-control'}),
			'nombreEmpresa': forms.TextInput(attrs={'class': 'form-control'}),
			'correoContacto': forms.EmailInput(attrs={'class': 'form-control'}),
			'direccion': forms.TextInput(attrs={'class': 'form-control'}),
			'telefonoContacto': forms.TextInput(attrs={'class': 'form-control'}),
			'telefonoEmpresa': forms.TextInput(attrs={'class': 'form-control'}),
		}

class ClienteForm(forms.ModelForm):

	class Meta:
		model = Cliente

		fields= [
			'rtn',
			'nombre',
			'apellido',
			'correo',
			'direccion',
			'telefono',
		]

		labels = {
			'rtn': 'RTN',
			'nombre': 'Nombre',
			'apellido': 'Apellido',
			'correo': 'Correo Electrónico',
			'direccion': 'Dirección',
			'telefono': 'Teléfono',

		}

		widgets = {
			'rtn': forms.TextInput(attrs={'class': 'form-control'}),
			'nombre': forms.TextInput(attrs={'class': 'form-control'}),
			'apellido': forms.TextInput(attrs={'class': 'form-control'}),
			'correo': forms.EmailInput(attrs={'class': 'form-control'}),
			'direccion': forms.TextInput(attrs={'class': 'form-control'}),
			'telefono': forms.TextInput(attrs={'class': 'form-control'}),
		}