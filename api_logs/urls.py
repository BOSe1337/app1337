from django.conf.urls.static import static
from django.urls import path

from api_logs.views import UserAccessView
from app1337 import settings

urlpatterns = [
    path("",UserAccessView.as_view()), #имортируем UserAccessView
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) #добавляем статику