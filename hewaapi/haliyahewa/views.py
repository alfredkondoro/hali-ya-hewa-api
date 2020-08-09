from django.shortcuts import render
from rest_framework import viewsets
from .models import Haliyahewa
from .serializers import HaliyahewaSerializer

class HaliyahewaView(viewsets.ModelViewSet):
	queryset = Haliyahewa.objects.all()
	serializer_class = HaliyahewaSerializer
