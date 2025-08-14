from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import UserViewSet
from .serializers import MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
