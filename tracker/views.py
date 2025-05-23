from django.shortcuts import render
from .models import Activity
from .serializers import ActivitySerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
# from .kafka_producer import send_activity_event

class ActivityView(APIView):

    def post(self, request, username):
        try:
            user = User.objects.get(username=username)

        except User.DoesNotExist as e:
            print(str(e))
            return Response(
                {"error": "User does dot exists. Please register first."},
                status=status.HTTP_404_NOT_FOUND,
            )
        data = request.data.copy()
        serializer = ActivitySerializer(data=data, context={"user": user})
        if serializer.is_valid():
            serializer.save()
            # send_activity_event(data)
            return Response(
                {"message": "activity recorded"}, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

