__author__ = 'gabriel'
import csv
import os
from models import Poi, TravelTime
from geodjango import settings
from django.contrib.gis.geos import Point
from django.contrib.gis.geos import GEOSGeometry
import json
from django.db import IntegrityError
import psycopg2
from django import db

DBNAME = settings.DATABASES['default']['NAME']

def populate_pois():

    conn = psycopg2.connect(database=DBNAME)
    cur = conn.cursor()
    sql = """SELECT rid, definitive, feature_co, geog FROM travel_time_data;"""
    cur.execute(sql)
    rows = cur.fetchall()
    bulk_list = []

    for row in rows:
        this_place = {
            'rid': int(row[0]),
            'def_name': row[1],
            'feature_type': row[2],
            'point': GEOSGeometry(row[3]),
        }
        m = Poi(**this_place)
        bulk_list.append(m)

    Poi.objects.bulk_create(bulk_list)


def populate_travel_times():

    conn = psycopg2.connect(database=DBNAME)
    cur = conn.cursor()
    sql = """SELECT rid, driving_dist_km, driving_time_mins, crow_dist_m FROM travel_time_data;"""
    cur.execute(sql)
    rows = cur.fetchall()
    bulk_list = []
    origin = Poi.objects.get(def_name='Salisbury')

    for row in rows:
        try:
            p = Poi.objects.get(rid=int(row[0]))
        except Exception:
            print "Failed to find Poi for rid %u" % int(row[0])
            pass

        this_tt = {
            'origin': origin,
            'destination': p,
            'travel_distance': row[1],
            'travel_time': row[2],
            'crow_distance': row[3],
        }
        m = TravelTime(**this_tt)
        bulk_list.append(m)

    TravelTime.objects.bulk_create(bulk_list)
