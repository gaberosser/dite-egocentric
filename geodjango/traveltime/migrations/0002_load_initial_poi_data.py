# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        # Note: Don't use "from appname.models import ModelName". 
        # Use orm.ModelName to refer to models in this application,
        # and orm['appname.ModelName'] for models in other applications.

        from django.core.management import call_command
        call_command("loaddata", "fixtures/initial_poi_data.json")

    def backwards(self, orm):
        "Write your backwards methods here."

    models = {
        u'traveltime.poi': {
            'Meta': {'object_name': 'Poi'},
            'def_name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'feature_type': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'point': ('django.contrib.gis.db.models.fields.PointField', [], {'geography': 'True'}),
            'rid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        u'traveltime.traveltime': {
            'Meta': {'object_name': 'TravelTime'},
            'crow_distance': ('django.db.models.fields.FloatField', [], {}),
            'destination': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tt_destination_set'", 'to': u"orm['traveltime.Poi']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'origin': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tt_origin_set'", 'to': u"orm['traveltime.Poi']"}),
            'travel_distance': ('django.db.models.fields.FloatField', [], {}),
            'travel_time': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['traveltime']
    symmetrical = True
