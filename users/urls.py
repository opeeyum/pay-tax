from urllib.parse import urlparse
from django import urls
from django.urls import path

from . import views

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name='signup'),
    path("profile/<str:pk>/", views.edit_user, name='edit_user'),
]
