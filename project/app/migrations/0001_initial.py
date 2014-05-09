# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Categoria'
        db.create_table(u'app_categoria', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'app', ['Categoria'])

        # Adding model 'Producto'
        db.create_table(u'app_producto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
            ('precio', self.gf('django.db.models.fields.FloatField')()),
            ('categoria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Categoria'])),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'app', ['Producto'])

        # Adding model 'Unidadpresentacion'
        db.create_table(u'app_unidadpresentacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
            ('cantidad', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'app', ['Unidadpresentacion'])

        # Adding model 'Proveedore'
        db.create_table(u'app_proveedore', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('razonsocial', self.gf('django.db.models.fields.TextField')()),
            ('rfc', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('contacto', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal(u'app', ['Proveedore'])

        # Adding model 'Materiaprima'
        db.create_table(u'app_materiaprima', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
            ('costo', self.gf('django.db.models.fields.FloatField')()),
            ('claveproveedor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Proveedore'])),
            ('clavepresentacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Unidadpresentacion'])),
        ))
        db.send_create_signal(u'app', ['Materiaprima'])

        # Adding model 'Cliente'
        db.create_table(u'app_cliente', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('apellidopaterno', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('apellidomaterno', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('rfc', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal(u'app', ['Cliente'])

        # Adding model 'Venta'
        db.create_table(u'app_venta', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('clavecliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Cliente'])),
            ('subtotal', self.gf('django.db.models.fields.FloatField')()),
            ('iva', self.gf('django.db.models.fields.FloatField')()),
            ('total', self.gf('django.db.models.fields.FloatField')()),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'app', ['Venta'])

        # Adding model 'Ventasproducto'
        db.create_table(u'app_ventasproducto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('claveproducto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Producto'])),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'app', ['Ventasproducto'])

        # Adding model 'Receta'
        db.create_table(u'app_receta', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('claveproducto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Producto'])),
            ('clavemateriaprima', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Materiaprima'])),
            ('cantidad', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'app', ['Receta'])


    def backwards(self, orm):
        # Deleting model 'Categoria'
        db.delete_table(u'app_categoria')

        # Deleting model 'Producto'
        db.delete_table(u'app_producto')

        # Deleting model 'Unidadpresentacion'
        db.delete_table(u'app_unidadpresentacion')

        # Deleting model 'Proveedore'
        db.delete_table(u'app_proveedore')

        # Deleting model 'Materiaprima'
        db.delete_table(u'app_materiaprima')

        # Deleting model 'Cliente'
        db.delete_table(u'app_cliente')

        # Deleting model 'Venta'
        db.delete_table(u'app_venta')

        # Deleting model 'Ventasproducto'
        db.delete_table(u'app_ventasproducto')

        # Deleting model 'Receta'
        db.delete_table(u'app_receta')


    models = {
        u'app.categoria': {
            'Meta': {'object_name': 'Categoria'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'app.cliente': {
            'Meta': {'object_name': 'Cliente'},
            'apellidomaterno': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'apellidopaterno': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'rfc': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'app.materiaprima': {
            'Meta': {'object_name': 'Materiaprima'},
            'clavepresentacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Unidadpresentacion']"}),
            'claveproveedor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Proveedore']"}),
            'costo': ('django.db.models.fields.FloatField', [], {}),
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'app.producto': {
            'Meta': {'object_name': 'Producto'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Categoria']"}),
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'precio': ('django.db.models.fields.FloatField', [], {})
        },
        u'app.proveedore': {
            'Meta': {'object_name': 'Proveedore'},
            'contacto': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'razonsocial': ('django.db.models.fields.TextField', [], {}),
            'rfc': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'app.receta': {
            'Meta': {'object_name': 'Receta'},
            'cantidad': ('django.db.models.fields.FloatField', [], {}),
            'clavemateriaprima': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Materiaprima']"}),
            'claveproducto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Producto']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'app.unidadpresentacion': {
            'Meta': {'object_name': 'Unidadpresentacion'},
            'cantidad': ('django.db.models.fields.FloatField', [], {}),
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'app.venta': {
            'Meta': {'object_name': 'Venta'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            'clavecliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Cliente']"}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iva': ('django.db.models.fields.FloatField', [], {}),
            'subtotal': ('django.db.models.fields.FloatField', [], {}),
            'total': ('django.db.models.fields.FloatField', [], {})
        },
        u'app.ventasproducto': {
            'Meta': {'object_name': 'Ventasproducto'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            'claveproducto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Producto']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['app']