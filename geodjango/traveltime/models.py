from django.contrib.gis.db import models

# Create your models here.
class Poi(models.Model):

    name = models.CharField(max_length=256, verbose_name='POI name')
    point = models.PointField(verbose_name='Location')

    # override default object manager to allow spatial queries
    objects = models.GeoManager()

    def __str__(self):
        """ The string that is used to identify an object in the interpreter """
        return self.name


class TravelTime(models.Model):

    origin = models.ForeignKey(Poi, verbose_name="Originating POI", related_name="tt_origin_set")
    destination = models.ForeignKey(Poi, verbose_name="Destination POI", related_name="tt_destination_set")
    travel_time = models.FloatField(verbose_name="Travel time")

    # override default object manager to allow spatial queries
    # not sure if needed for this model?
    objects = models.GeoManager()

    def __str__(self):
        return "%s -> %s" % (self.origin.name, self.destination.name)