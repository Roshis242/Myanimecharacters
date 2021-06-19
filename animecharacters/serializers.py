from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Animecharacter

class Animecharacterserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Animecharacter
        fields = '__all__'