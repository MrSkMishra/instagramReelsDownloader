from rest_framework import serializers

class LinkSerializer(serializers.Serializer):
    link = serializers.URLField()

class ImageUploadSerializer(serializers.Serializer):
    image = serializers.ImageField()