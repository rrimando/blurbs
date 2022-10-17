from rest_framework import routers, serializers, viewsets
from .models import Blurb


class BlurbSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blurb
        fields = ["id", "name", "blurb", "created_at"]
