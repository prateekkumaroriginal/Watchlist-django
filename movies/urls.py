from django.urls import path, reverse
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index")
]
