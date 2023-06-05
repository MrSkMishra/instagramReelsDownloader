from django.shortcuts import render
from .downloader import *
from django.http import JsonResponse,HttpResponse
import wget
import os
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import LinkSerializer

@api_view(['POST'])
def download_video(request):
    serializer = LinkSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    link = serializer.validated_data['link']
    video_link = ReturnVideoLink(link)
    return Response({'link': video_link})
