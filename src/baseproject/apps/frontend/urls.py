from django.urls import path

from . import views

urlpatterns = [
    # html pages
    path("", views.HomepageView.as_view(), name="homepage"),
]
