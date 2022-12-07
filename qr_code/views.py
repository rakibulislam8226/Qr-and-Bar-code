from .serializers import QRCodeSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class QRCodeAPIView(APIView):
    serializer_class = QRCodeSerializer
    def post(self, request):
        serializer = QRCodeSerializer(data=request.data, context={'request': request})
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