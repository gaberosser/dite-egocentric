from django.contrib.gis.db import models


# Create your models here.
class Poi(models.Model):

    CITY = 'C'
    TOWN = 'T'
    HILL = 'H'
    OTHER = 'O'

    FEATURE_TYPE_CHOICES = [
        (CITY, 'city'),
        (TOWN, 'town'),
        (HILL, 'hill/mountain'),
        (OTHER, 'other'),
    ]

    rid = models.IntegerField(primary_key=True)
    def_name = models.CharField(max_length=256, verbose_name='POI name') # TODO: make unique, once data are clean
    point = models.PointField(verbose_name='Location', geography=True)
    feature_type = models.CharField(max_length=64, choices=FEATURE_TYPE_CHOICES)

    # override default object manager to allow spatial queries
    objects = models.GeoManager()

    def __str__(self):
        """ The string that is used to identify an object in the interpreter """
        return self.def_name


class TravelTime(models.Model):

    origin = models.ForeignKey(Poi, verbose_name="Originating POI", related_name="tt_origin_set")
    destination = models.ForeignKey(Poi, verbose_name="Destination POI", related_name="tt_destination_set")
    travel_time = models.FloatField(verbose_name="Travel time")
    travel_distance = models.FloatField(verbose_name="Travel distance")
    crow_distance = models.FloatField(verbose_name="Crow's line distance")

    # override default object manager to allow spatial queries
    # not sure if needed for this model?
    objects = models.GeoManager()

    def __str__(self):
        return "%s -> %s" % (self.origin.def_name, self.destination.def_name)