__author__ = 'gabriel'
import csv
import os
from models import Poi
from geodjango import settings
from django.contrib.gis.geos import Point
from django.db import IntegrityError


def populate_pois():

    DATA_PATH = os.path.join(settings.DATA_DIR, '50kgaz2013.txt')

    with open(DATA_PATH, 'r') as f:
        c = csv.reader(f, delimiter=':')
        save_count = 0
        for row in c:
            feature_type = row[14]
            if feature_type not in [Poi.CITY, Poi.TOWN]:
                continue
            name = row[2].decode('windows-1252')
            northing = int(row[8])
            easting = int(row[9])
            m = Poi(def_name=name, feature_type=feature_type, point=Point(northing, easting))
            try:
                m.save()
                save_count += 1
            except IntegrityError as exc:
                # duplicate error, ignore, could update here instead
                # print repr(exc)
                continue


    print "Saved %d poi objects" % save_count