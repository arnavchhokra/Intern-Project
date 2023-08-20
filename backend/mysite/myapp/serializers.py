
from rest_framework import serializers

class ThreadSerializer(serializers.Serializer):
    title = serializers.CharField()
    author = serializers.CharField()
    url = serializers.URLField()