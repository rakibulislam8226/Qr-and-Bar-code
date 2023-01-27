from django.urls import path
from . import views
urlpatterns = [
    path('bar_code/', views.BarCodeAPIView.as_view(), name='bar_code'),
]