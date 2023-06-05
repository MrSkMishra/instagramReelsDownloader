from rest_framework import serializers

class LinkSerializer(serializers.Serializer):
    link = serializers.URLField()