from django.shortcuts import render

# Create your views here.
from .serializers import Bar_codeSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class BarCodeAPIView(APIView):
    serializer_class = Bar_codeSerializer
    def post(self, request):
        serializer = Bar_codeSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status' : True,
                'message' : 'Success',
                'Data' : serializer.data},
                status=status.HTTP_201_CREATED)
        else :
            return Response({
                'status' : False,
                'message' : "Error"},
                status = status.HTTP_400_BAD_REQUEST)