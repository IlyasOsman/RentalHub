from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="RentalHub API",
        default_version="v1",
        description="An Apartment Management API for Real Estate",
        contact=openapi.Contact(email="earlyosman@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path(settings.ADMIN_URL, admin.site.urls),
    path("api/v1/auth/", include("djoser.urls")),
    path("api/v1/auth/", include("core.users.urls")),
    path("api/v1/profiles/", include("core.profiles.urls")),
    path("api/v1/apartments/", include("core.apartments.urls")),
    path("api/v1/issues/", include("core.issues.urls")),
    path("api/v1/reports/", include("core.reports.urls")),
    path("api/v1/ratings/", include("core.ratings.urls")),
    path("api/v1/posts/", include("core.posts.urls")),
]

admin.site.site_header = "RentalHub Admin"
admin.site.site_title = "RentalHub Admin Portal"
admin.site.index_title = "Welcome to RentalHub Admin Portal"