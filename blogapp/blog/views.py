from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

class SampleAPI(APIView):
    permission_classes = []
    def get(self, request):
        return Response({'hello':'hello'})
    
    def post(self, request):
        return Response({'asdasda':'adadasd'})