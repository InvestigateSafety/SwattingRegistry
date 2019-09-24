from django.contrib.gis.db import models
from django.contrib.postgres.operations import CreateExtension
from django.db import migrations
from django.contrib.postgres.fields import JSONField

class Household(models.Model):
    """A model of a household."""
    name1 = models.CharField(max_length=200)
    phone1 = models.CharField(max_length=200)
    name2 = models.CharField(max_length=200, blank=True)
    phone2 = models.CharField(max_length=200, blank=True)
    name3 = models.CharField(max_length=200, blank=True)
    phone3 = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=200)
    were_threats_made = models.BooleanField()
    police_contacted = models.BooleanField()
    in_rave = models.BooleanField()
    in_police_backend = models.BooleanField()
    has_been_swatted = models.BooleanField()
    address = models.CharField(max_length=200)
    point = models.PointField()
    streaming_url = models.CharField(max_length=200, blank=True)
    concerns = models.TextField(blank=True)
    place_details = models.TextField(blank=True)
    data = JSONField(null=True,blank=True)
