# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'MateriaPrima.claveproveedor'
        db.delete_column(u'app_materiaprima', 'claveproveedor_id')

        # Adding field 'MateriaPrima.existencia'
        db.add_column(u'app_materiaprima', 'existencia',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'MateriaPrima.claveproveedor'
        db.add_column(u'app_materiaprima', 'claveproveedor',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['app.Proveedore']),
                      keep_default=False)

        # Deleting field 'MateriaPrima.existencia'
        db.delete_column(u'app_materiaprima', 'existencia')


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
            'Meta': {'object_name': 'MateriaPrima'},
            'clavepresentacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.UnidadPresentacion']"}),
            'costo': ('django.db.models.fields.FloatField', [], {}),
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'existencia': ('django.db.models.fields.FloatField', [], {}),
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
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True'}),
            'productos': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['app.MateriaPrima']", 'symmetrical': 'False'}),
            'razonsocial': ('django.db.models.fields.TextField', [], {'primary_key': 'True'}),
            'rfc': ('django.db.models.fields.CharField', [], {'default': "'123'", 'max_length': '50'}),
            'telefono': ('django.db.models.fields.CharField', [], {'default': "'55'", 'max_length': '30', 'null': 'True'})
        },
        u'app.receta': {
            'Meta': {'object_name': 'Receta'},
            'cantidad': ('django.db.models.fields.FloatField', [], {}),
            'clavemateriaprima': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['app.MateriaPrima']", 'symmetrical': 'False'}),
            'claveproducto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Producto']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'app.unidadpresentacion': {
            'Meta': {'object_name': 'UnidadPresentacion'},
            'cantidad': ('django.db.models.fields.FloatField', [], {}),
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'unidmedida': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'app.venta': {
            'Meta': {'object_name': 'Venta'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            'clavecliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Cliente']"}),
            'claveproducto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Producto']"}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iva': ('django.db.models.fields.FloatField', [], {}),
            'subtotal': ('django.db.models.fields.FloatField', [], {}),
            'total': ('django.db.models.fields.FloatField', [], {})
        },
        u'app.ventasproducto': {
            'Meta': {'object_name': 'VentasProducto'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            'claveproducto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Producto']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['app']