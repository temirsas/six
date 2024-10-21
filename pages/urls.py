from django.urls import path # type: ignore
from .views import HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
]
