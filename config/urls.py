from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("", include("apps.dashboard.urls")),
    path("incidents/", include("apps.incidents.urls")),
    path("risk-assessments/", include("apps.risk.urls")),
    path("inspections/", include("apps.inspections.urls")),
    path("ppe/", include("apps.ppe.urls")),
    path("fire-equipment/", include("apps.fire.urls")),
    path("training/", include("apps.training.urls")),
    path("capa/", include("apps.capa.urls")),
    path("doshs-reports/", include("apps.doshs.urls")),
    path("notifications/", include("apps.notifications.urls")),
    path("accounts/", include("apps.accounts.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
