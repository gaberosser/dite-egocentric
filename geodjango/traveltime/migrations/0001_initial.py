# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Poi'
        db.create_table(u'traveltime_poi', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('point', self.gf('django.contrib.gis.db.models.fields.PointField')()),
        ))
        db.send_create_signal(u'traveltime', ['Poi'])

        # Adding model 'TravelTime'
        db.create_table(u'traveltime_traveltime', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('origin', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tt_origin_set', to=orm['traveltime.Poi'])),
            ('destination', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tt_destination_set', to=orm['traveltime.Poi'])),
            ('travel_time', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'traveltime', ['TravelTime'])


    def backwards(self, orm):
        # Deleting model 'Poi'
        db.delete_table(u'traveltime_poi')

        # Deleting model 'TravelTime'
        db.delete_table(u'traveltime_traveltime')


    models = {
        u'traveltime.poi': {
            'Meta': {'object_name': 'Poi'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'point': ('django.contrib.gis.db.models.fields.PointField', [], {})
        },
        u'traveltime.traveltime': {
            'Meta': {'object_name': 'TravelTime'},
            'destination': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tt_destination_set'", 'to': u"orm['traveltime.Poi']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'origin': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tt_origin_set'", 'to': u"orm['traveltime.Poi']"}),
            'travel_time': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['traveltime']