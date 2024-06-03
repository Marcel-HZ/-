from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from myApp.views import RegisterViewSet
from rest_framework_jwt.views import obtain_jwt_token

router = DefaultRouter()    
router.register(r'register', RegisterViewSet)

urlpatterns = [
    # path('login/', UserApi.as_view({'post': 'login'})),
    path('login/', obtain_jwt_token),
    re_path('^', include(router.urls))
]
