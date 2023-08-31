from django.shortcuts import render
from .downloader import *
from django.http import JsonResponse,HttpResponse
import wget
import os
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import LinkSerializer
from rembg import remove
from PIL import Image
from .serializers import ImageUploadSerializer
from rest_framework.views import APIView
from io import BytesIO



@api_view(['POST'])
def download_video(request):
    serializer = LinkSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    link = serializer.validated_data['link']
    video_link = ReturnVideoLink(link)
    return Response({'link': video_link})

# class RemoveBackgroundView(APIView):
#     def post(self, request, format=None):
#         serializer = ImageUploadSerializer(data=request.data)
#         if serializer.is_valid():
#             image = serializer.validated_data['image']
#             input_image = Image.open(image)
#             output_image = remove(input_image)
            
#             response = HttpResponse(content_type='image/png')
#             output_image.save(response, 'PNG')
#             return response
#         else:
#             return Response(serializer.errors, status=400)

class RemoveBackgroundView(APIView):
    def post(self, request, format=None):
        serializer = ImageUploadSerializer(data=request.data)
        if serializer.is_valid():
            image = serializer.validated_data['image']
            input_image = Image.open(image)
            output_image = remove(input_image)
            
            output_io = BytesIO()
            output_image.save(output_io, 'PNG')
            
            response = HttpResponse(output_io.getvalue(), content_type='image/png')
            response['Content-Disposition'] = 'attachment; filename=output.png'
            return response
        else:
            return Response(serializer.errors, status=400)