from django.urls import path

from api_logs.views import UserAccessView

urlpatterns = [
    path("",UserAccessView.as_view()), #имортируем UserAccessView
]