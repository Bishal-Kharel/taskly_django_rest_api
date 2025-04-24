from django.contrib.auth.models import User

from rest_framework import viewsets
from .serializers import UserSerializer
from .permissions import IsUserOwnerOrGetAnPostOnly

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsUserOwnerOrGetAnPostOnly,]
    queryset = User.objects.all()
    serializer_class = UserSerializer
