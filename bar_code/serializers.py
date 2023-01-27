from rest_framework import serializers
from .models import Bar_code

class Bar_codeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bar_code
        fields = '__all__'
        extra_kwargs = {
        'bar_code': {'read_only': True},
    }