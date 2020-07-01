from django.urls import path
from oauth2_provider import views

urlpatterns = [
    path("token/", views.TokenView.as_view(), name="token"),
    path("revoke_token/", views.RevokeTokenView.as_view(), name="revoke-token"),
    path("introspect/", views.IntrospectTokenView.as_view(), name="introspect"),
]