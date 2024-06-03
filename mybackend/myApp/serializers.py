from myApp.models import FisherMan
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

from rest_framework_jwt.settings import api_settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class FisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = FisherMan
        fields = '__all__'

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        print(username, password)
        user = FisherMan.objects.filter(username=username)
        if user and check_password(password, user.password):
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            self.context['token'] = token
            self.context['username'] = username
            self.context['id'] = user.id
            return attrs
        else:
            raise serializers.ValidationError('用户名或密码错误')


