from rest_framework import viewsets, mixins
from .serializers import HeroSerializer
from .models import Hero

class HeroViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet):
    queryset = Hero.objects.all().order_by('id')
    serializer_class = HeroSerializer
