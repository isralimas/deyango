# -*- encoding: utf-8 -*-
from django.db import models
from choices import *

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    def __unicode__(self):
		return self.nombre

class Producto(models.Model):
	nombre = models.CharField(max_length=50)
	descripcion = models.TextField()
	precio = models.FloatField()
	categoria = models.ForeignKey('Categoria')
	cantidad = models.IntegerField()
	def __unicode__(self):
			return str(self.id) + ' ' + self.nombre + ' ' + str(self.precio)


class UnidadPresentacion(models.Model):
	descripcion = models.TextField()
	unidmedida = models.CharField('Unidad de medida', max_length=20, choices=unidadesDmedida)
	cantidad = models.FloatField()
	def __unicode__(self):
		return str(self.id) + ' ' + self.descripcion + ' ' + str(self.cantidad)


class Proveedore(models.Model):
	razonsocial = models.TextField(help_text='Ingresa una razon social', primary_key=True)
	rfc = models.CharField(max_length=50, default='123')
	direccion = models.CharField(max_length=80, blank= True)
	telefono = models.CharField('Teléfono', max_length=30, default='55', null=True)
	contacto = models.CharField(max_length=50, choices=proveedores)
	email = models.CharField(max_length=40, null=True)
	productos = models.ManyToManyField('MateriaPrima', related_name="proveedore_materia_prima")
	def __unicode__(self):
		return self.razonsocial

class MateriaPrima(models.Model):
	descripcion = models.TextField()
	costo = models.FloatField()
	existencia = models.FloatField()
	clavepresentacion = models.ForeignKey('UnidadPresentacion')
	def __unicode__(self):
		return str(self.id) + ' ' + self.descripcion + ' ' + str(self.costo)


class Cliente(models.Model):
	nombre = models.CharField(max_length=50)
	apellidopaterno = models.CharField(max_length=50)
	apellidomaterno = models.CharField(max_length=50)
	rfc = models.CharField(max_length=50)
	direccion = models.CharField(max_length=80)
	telefono = models.CharField(max_length=30)
	email = models.CharField(max_length=40)	
	def __unicode__(self):
		return str(self.id) + ' ' + self.nombre

class Venta(models.Model):
	fecha = models.DateTimeField(auto_now_add=True)
	claveproducto = models.ForeignKey("Producto")
	clavecliente = models.ForeignKey("Cliente")
	subtotal = models.FloatField()
	iva = models.FloatField()
	total = models.FloatField()
	cantidad = models.IntegerField()
	def __unicode__(self):
		return str(self.id) + ' ' + self.claveproducto.nombre + ' ' +str(self.subtotal) + ' '+str(self.iva) + ' '+str(self.total) + ' '+str(self.cantidad)

class VentasProducto(models.Model):
	claveproducto = models.ForeignKey("Producto")
	cantidad = models.IntegerField()
	def __unicode__(self):
		return str(self.id) + ' ' + self.claveproducto.nombre + ' ' + str(self.cantidad)


class Receta(models.Model):
	claveproducto = models.ForeignKey("Producto")
	clavemateriaprima = models.ManyToManyField("MateriaPrima")
	cantidad= models.FloatField()
	def __unicode__(self):
		return str(self.id) + ' ' + self.claveproducto.nombre


