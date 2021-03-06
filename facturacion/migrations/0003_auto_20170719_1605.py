# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-19 22:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0002_auto_20170719_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleFactura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
        migrations.RemoveField(
            model_name='factura',
            name='producto',
        ),
        migrations.AddField(
            model_name='detallefactura',
            name='factura',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facturacion.Factura'),
        ),
        migrations.AddField(
            model_name='detallefactura',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facturacion.Producto'),
        ),
    ]
