from rest_framework import serializers
from .models import Haliyahewa

class HaliyahewaSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Haliyahewa
		fields = ('id','url', 'mkoa','mvua', 'nyuzi')