from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.company, name = "company"),
    path("A/", views.A, name="A"),
    path("insert/", views.insert, name="insert"),
    path('<int:A_id>', views.detail, name='detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
