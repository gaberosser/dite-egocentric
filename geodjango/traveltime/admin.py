from django.contrib.gis import admin
from models import Poi, TravelTime


class PoiAdmin(admin.GeoModelAdmin):
    search_fields = ['rid', 'def_name']
    list_filter = ['feature_type']


admin.site.register(Poi, PoiAdmin)
admin.site.register(TravelTime, admin.GeoModelAdmin)