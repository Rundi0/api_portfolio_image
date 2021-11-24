from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Comment, Image, Portfolio

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"


class PortfolioSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    class Meta:
        model = Portfolio
        fields = "__all__"


class RootImageSerializer(serializers.ModelSerializer):
    portfolio = serializers.SlugRelatedField(slug_field="name", read_only=True)
    class Meta:
        model = Image
        fields = ("image", "name", "description", "portfolio")


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
