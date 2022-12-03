from rest_framework.serializers import ModelSerializer
from .models import URL

class URLShortnerSerializer(ModelSerializer):
    class Meta:
        model=URL
        fields='__all__'