from django.shortcuts import render

# Create your views here.
from .serializers import Animecharacterserializer
from .models import Animecharacter

from rest_framework import viewsets
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated

class Animecharacterviewset(viewsets.ModelViewSet):
    queryset = Animecharacter.objects.all().order_by('-id')
    serializer_class = Animecharacterserializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated] 