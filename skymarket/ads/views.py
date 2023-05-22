from django.shortcuts import get_object_or_404
from rest_framework import pagination, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework import permissions

from .models import Ad, Comment
from .filters import AdFilter
from .serializers import AdSerializer, CommentSerializer
from .permissions import IsAdmin


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    pagination_class = AdPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdFilter
    serializer_class = AdSerializer

    # def get_queryset(self):
    #     if self.action == 'me':
    #         return Ad.objects.filter(author=self.request.user).all()
    #     return Ad.objects.all()

    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'create', 'me']:
            self.permission_classes = [IsAdmin]
        else:
            self.permission_classes = [IsAdmin]
        return super().get_permissions()

    # def get_serializer_class(self):
    #     if self.action == 'retrieve':
    #         return AdSerializer
    #     return AdSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=False, methods=['get'])
    def me(self, request, *args, **kwargs):
        # self.queryset = Ad.objects.filter(author=request.user)
        return super().list(request, *args, **kwargs)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        if self.request.method == 'GET':
        # ad_instance = get_object_or_404(Ad, ad_id=self.kwargs['ad_pk'])
            return Comment.objects.filter(ad_id=self.kwargs['ad_pk'])
            # return ad_instance.comment_set.all()

    def perform_create(self, serializer):
        ad_instance = get_object_or_404(Ad, pk=self.kwargs['ad_pk'])
        user = self.request.user
        serializer.save(author=user, ad=ad_instance)
