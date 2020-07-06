from allauth.account import app_settings as allauth_settings
from allauth.account.utils import complete_signup
from oauth2_provider.views.generic import InitializationMixin
from oauth2_provider.views.mixins import ScopedResourceMixin, ProtectedResourceMixin
from rest_auth.registration.views import RegisterView
from rest_framework.viewsets import ModelViewSet


class CustomRegisterView(RegisterView):

    def perform_create(self, serializer):
        user = serializer.save(self.request)
        complete_signup(self.request._request, user, allauth_settings.EMAIL_VERIFICATION, None)
        return user


class CustomScopedProtectedResourceViewSet(ScopedResourceMixin, ProtectedResourceMixin,
                                           InitializationMixin, ModelViewSet):
    pass