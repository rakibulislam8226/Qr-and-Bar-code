from django.urls import path
from . import views
urlpatterns = [
    path('qr_code/', views.QRCodeAPIView.as_view(), name='qr_code'),
]