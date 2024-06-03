from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ViewSet
from myApp.models import FisherMan
from myApp.serializers import FisherSerializer, UserDetailSerializer
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


# Create your views here.
class FiserViewSet(ModelViewSet):
    queryset = FisherMan.objects.all
    serializer_class = FisherSerializer

def jwt_response_payload_handler(token, user=None, request=None):
    """
    设置jwt登录之后返回token和user信息
    """
    fisherman = FisherMan.objects.get(user=user)
    return {
        'token': token,
        'user': UserDetailSerializer(user, context={'request': request}).data,
        'fisherman': FisherSerializer(fisherman, context={'request': request}).data
    }

# class UserApi(viewsets.ViewSet):
#     """
#     用户注册
#     """
class RegisterViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    用户注册
    """
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

    # def login(self, request):
    #     user = FisherMan.objects.filter(username=request.data['username'])
    #     if user and check_password(request.data['password'], user.password):
    #         # 生成token
    #         token, created = Token.objects.get_or_create(user=user)
    #         return Response({
    #             'msg': '登录成功', 
    #             'user': FisherSerializer(user, context={'request': request}).data, 
    #             'token': token.key
    #             })

    def create(self, request, *args, **kwargs):
        user = User.objects.filter(username=request.data['username'])
        if user:
            return Response({'msg': '用户名已存在'}, status=status.HTTP_201_CREATED)
        user_detail = UserDetailSerializer(data=request.data)
        if user_detail.is_valid():
            user_detail.save()
        user = User.objects.get(username=request.data['username'])
        # 密码转成密文存储
        user.password = make_password(user.password)
        user.save()
        fisherMan = FisherMan(user=user, name=request.data['name'], phone=request.data['phone'], email=request.data['email'])
        if fisherMan:
            fisherMan.save()
            return Response({'msg': '注册成功'}, status=status.HTTP_200_OK)
        return Response(user_detail.errors)