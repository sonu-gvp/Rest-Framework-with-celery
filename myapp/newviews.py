from myapp.models import Register
from myapp.serializers import RegisterSerializer, UserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.models import User

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from . import tasks

from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from . models import TaskDetails

class RegisterList(APIView):
    """
    List all Register, or create a new Register.
    """
    def get(self, request, format=None):
        if request.user.is_authenticated:
            snippets = Register.objects.all()
            serializer = RegisterSerializer(snippets, many=True)
            tasks.first()
            # task = TaskDetails()
            # user = User.objects.get(id=request.user.id)
            # task.user_task = user
            # result  = tasks.first()
            # task_id = result.task_id
            # task.task_id = task_id
            # task.save()
            return Response(serializer.data)

    def post(self, request, format=None):
        if request.user.is_authenticated:
            serializer = RegisterSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class RegisterDetail(APIView):
    """
    Retrieve, update or delete a Register instance.
    """
    def get_object(self, pk):
        try:
            return Register.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        if request.user.is_authenticated:
            snippet = self.get_object(pk)
            serializer = RegisterSerializer(snippet)
            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def put(self, request, pk, format=None):
        if request.user.is_authenticated:
            snippet = self.get_object(pk)
            serializer = RegisterSerializer(snippet, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, pk, format=None):
        if request.user.is_authenticated:
            snippet = self.get_object(pk)
            snippet.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_401_UNAUTHORIZED)



@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)