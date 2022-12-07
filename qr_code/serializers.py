from rest_framework import serializers
from .models import QrCode

class QRCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QrCode
        fields = '__all__'
        extra_kwargs = {
        'qr_code': {'read_only': True},
    }