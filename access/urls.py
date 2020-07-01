from django.urls import path
from oauth2_provider import views

urlpatterns = [

    path("authorize/", views.AuthorizationView.as_view(), name="authorize"),

    # Applications management views
    path("applications/", views.ApplicationList.as_view(), name="list"),
    path("applications/register/", views.ApplicationRegistration.as_view(), name="register"),
    path("applications/<pk>/", views.ApplicationDetail.as_view(), name="detail"),
    path("applications/<pk>/delete/", views.ApplicationDelete.as_view(), name="delete"),
    path("applications/<pk>/update/", views.ApplicationUpdate.as_view(), name="update"),

    # Token management views
    path("authorized_tokens/", views.AuthorizedTokensListView.as_view(), name="authorized-token-list"),
    path("authorized_tokens/<pk>/delete/", views.AuthorizedTokenDeleteView.as_view(), name="authorized-token-delete")

]