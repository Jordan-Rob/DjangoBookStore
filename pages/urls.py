from django.urls import path

from .views import HomePgView, AboutPgView

urlpatterns = [
    path('', HomePgView.as_view(), name='home'),
    path('about/', AboutPgView.as_view(), name='about')
]
