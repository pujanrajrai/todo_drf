from django.contrib import auth
from django.shortcuts import render
from rest_framework.response import Response

from .models import User
from rest_framework.views import APIView
from .serializers import RegisterSerializers


# Create your views here.

class RegisterAPIView(APIView):
    def post(self, request):
        try:
            data = request.data.copy()
            serializer = RegisterSerializers(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': 200,
                    'message': 'User Created Successfully Please Login',
                }
                )
            else:
                return Response({
                    'status': 400,
                    'data': serializer.errors,
                }
                )
        except Exception as e:
            print(e)
            return Response({
                'status': 400,
                'message': 'Something Went Wrong',
            }
            )
