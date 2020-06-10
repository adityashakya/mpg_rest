from rest_framework import serializers
from .models import MPG

class mpgSerializer(serializers.ModelSerializer):
    class Meta:
        model = MPG
        fields = '__all__'

