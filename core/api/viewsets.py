from allauth.account import app_settings as allauth_settings
from allauth.account.utils import complete_signup
from rest_auth.registration.views import RegisterView


class RegisterView(RegisterView):

    def perform_create(self, serializer):
        user = serializer.save(self.request)
        complete_signup(self.request._request, user, allauth_settings.EMAIL_VERIFICATION, None)
        return user
