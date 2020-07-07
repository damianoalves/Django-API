from allauth.account import app_settings as allauth_settings
from allauth.account.utils import complete_signup
from django.http import Http404
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from oauth2_provider.views.generic import InitializationMixin
from oauth2_provider.views.mixins import ScopedResourceMixin, ProtectedResourceMixin
from rest_auth.registration.views import RegisterView
from rest_framework.viewsets import ModelViewSet

from core.errors import ViewPermissionDenied, CreatePermissionDenied, UpdatePermissionDenied, ObjectNotFound, \
    DestroyPermissionDenied
from core.utils import check_read_permission, check_create_permission, check_update_permission, check_delete_permission


class CustomRegisterView(RegisterView):

    def perform_create(self, serializer):
        user = serializer.save(self.request)
        complete_signup(self.request._request, user, allauth_settings.EMAIL_VERIFICATION, None)
        return user


class BaseViewSet(ModelViewSet):

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    ordering_fields = '__all__'
    lookup_field = 'uuid'

    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise ObjectNotFound

    def format_post_data(self):
        self.request.POST._mutable = True
        self.request.data['created_by'] = self.request.user.id
        self.request.data['updated_by'] = self.request.user.id
        self.request.data['user'] = self.request.user.id

    def format_update_data(self):
        self.request.POST._mutable = True
        self.request.data['updated_by'] = self.request.user.id

    def check_view_permission(self):
        instance = self.get_object()
        if not check_read_permission(self.request.user, instance):
            raise ViewPermissionDenied

    def check_create_permission(self):
        instance = self.get_object()
        if not check_create_permission(self.request.user, instance):
            raise CreatePermissionDenied

    def check_update_permission(self):
        instance = self.get_object()
        if not check_update_permission(self.request.user, instance):
            raise UpdatePermissionDenied

    def check_delete_permission(self):
        instance = self.get_object()
        if not check_delete_permission(self.request.user, instance):
            raise DestroyPermissionDenied

    def paginate_queryset(self, queryset):
        if self.paginator and self.request.query_params.get(self.paginator.page_query_param, None) is None:
            return None
        return super().paginate_queryset(queryset)

    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)
        for query in queryset:
            if not check_read_permission(self.request.user, query):
                queryset = queryset.exclude(id=query.id)
        return queryset

    def create(self, request, *args, **kwargs):
        self.format_post_data()
        return super(BaseViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        self.format_update_data()
        return super(BaseViewSet, self).update(request, *args, **kwargs)


class ProtectedScopedMixin(ScopedResourceMixin, ProtectedResourceMixin, InitializationMixin):
    pass


class CustomScopedProtectedResourceViewSet(ProtectedScopedMixin, BaseViewSet):
    pass