from .views import ActivityView
from django.urls import path

urlpatterns = [
    path("user/<str:username>/activity", ActivityView.as_view(), name="Activity Tracker View")
]
