from django.conf import settings
from django.http import HttpResponse, JsonResponse
from rest_framework import serializers
from rest_framework.response import Response
import rest_framework
import json
from rest_framework import viewsets
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from .models import User
from django.core import serializers
from .serializers import UserSerializer
from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
# Create your views here.



class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

 

class VerifyTokenView(TokenVerifyView):
    def post(self,request,*args,**kwargs):
        token = request.data['token']
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            valid_data = tokenBackend.decode(token,verify=False)
            serializer.validated_data['UserId'] = valid_data['user_id']
            print(serializer.validated_data['UserId'])
            user = User.objects.get(pk=valid_data['user_id'])
            data = serializers.serialize('json', [user,])
            struct = json.loads(data)
            struct[0]['fields']['password']=''
            serializer.validated_data['user'] = struct[0]['fields']
            #serializer.validated_data['user']= userResponse
            

        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)