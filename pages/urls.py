from django.urls import path

from .views import HomePgView

urlpatterns = [
    path('', HomePgView.as_view(), name='home')
]
