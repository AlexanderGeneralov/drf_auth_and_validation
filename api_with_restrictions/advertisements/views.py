from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from advertisements.models import Advertisement
from advertisements.serializers import AdvertisementSerializer
from advertisements.permissions import IsCreatorOrReadOnly
from advertisements.filters import AdvertisementFilter
from django_filters import rest_framework


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filterset_class = AdvertisementFilter
    filter_backends = (rest_framework.DjangoFilterBackend,)

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ['list', 'retrieve']:
            return []
        if self.action in ["create"]:
            return [IsAuthenticated()]
        if self.action in ["update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsCreatorOrReadOnly()]
        return []
