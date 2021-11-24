from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny, BasePermission

from .serializers import RegisterSerializer, UserSerializer


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.id == request.user.id
        

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class UserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    permission_classes = (IsOwner,)
    serializer_class = UserSerializer