from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Video
from .serializers import VideoSerializer
from django.http import Http404


# Create your views here.
class ListVideo(APIView):
    def get(self, request):
        videos = Video.objects.all()
        video_json = VideoSerializer(videos, many=True)
        return Response(video_json.data)

    def post(self, request):
        video_json = VideoSerializer(data=request.data)
        if video_json.is_valid():
            video_json.save()
            return Response(video_json.data, status=201)
        return Response(video_json.errors, status=400)


class DetailVideo(APIView):
    def get_object(self, id):
        try:
            return Video.objects.get(pk=id)
        except Video.DoesNotExist:
            raise Http404

    def get(self, request, id):
        video = self.get_object(id)
        video_json = VideoSerializer(video)
        return Response(video_json.data)

    def put(self, request, id):
        video = self.get_object(id)
        video_json = VideoSerializer(video, data=request.data)
        if video_json.is_valid():
            video_json.save()
            return Response(video_json.data)
        return Response(video_json.errors, status=400)

    def delete(self, request, id):
        video = self.get_object(id)
        video.delete()
        return Response(status=204)