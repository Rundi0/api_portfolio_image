from django.shortcuts import render
from rest_framework import generics, filters
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, BasePermission, SAFE_METHODS

from .serializers import CommentSerializer, ImageSerializer, PortfolioSerializer, RootImageSerializer
from .models import Comment, Image, Portfolio


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user


class IsOwnerOrReadOnlyImage(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.portfolio.author == request.user


class PortfolioListView(generics.ListCreateAPIView):
    queryset = Portfolio.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = PortfolioSerializer


class PortfolioView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Portfolio.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)
    serializer_class = PortfolioSerializer


class ImageListView(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    permission_classes = (IsOwnerOrReadOnlyImage,)
    serializer_class = ImageSerializer


class ImageView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    permission_classes = (IsOwnerOrReadOnlyImage,)
    serializer_class = ImageSerializer


class RootImageListView(generics.ListAPIView):
    queryset = Image.objects.order_by('-created_date')
    permission_classes = (AllowAny,)
    serializer_class = RootImageSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'description', 'portfolio__name')


class CommentView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = CommentSerializer