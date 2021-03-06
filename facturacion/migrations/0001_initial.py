# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-19 21:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rtn', models.CharField(blank=True, max_length=16, null=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('correo', models.CharField(max_length=50)),
                ('direccion', models.TextField()),
                ('telefono', models.CharField(blank=True, max_length=9, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DetalleFactura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facturacion.Cliente')),
                ('detalle', models.ManyToManyField(to='facturacion.DetalleFactura')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('stockMinimo', models.IntegerField()),
                ('existencia', models.IntegerField()),
                ('precioCosto', models.DecimalField(decimal_places=2, max_digits=7)),
                ('precioVenta', models.DecimalField(decimal_places=2, max_digits=7)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facturacion.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rtn', models.CharField(max_length=16)),
                ('nombreContacto', models.CharField(max_length=70)),
                ('nombreEmpresa', models.CharField(max_length=50)),
                ('correoContacto', models.CharField(max_length=70)),
                ('direccion', models.TextField()),
                ('telefonoContacto', models.CharField(blank=True, max_length=9, null=True)),
                ('telefonoEmpresa', models.CharField(blank=True, max_length=9, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facturacion.Proveedor'),
        ),
        migrations.AddField(
            model_name='detallefactura',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facturacion.Producto'),
        ),
    ]
