from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TestSerializer
from .models import Test


class TestDetails(APIView):
    def get_object(self, code):
        try:
            return Test.objects.get(code=code)
        except Test.DoesNotExist:
            raise Http404

    def get(self, request, code, format=None):
        snippet = self.get_object(code)
        serializer = TestSerializer(snippet)
        return Response(serializer.data)

    def post(self, request, code, format=None):
        print('TESTTTTTTTTTTT', request.data)
        serializer = TestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
