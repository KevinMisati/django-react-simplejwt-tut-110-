from django.urls import path,include
from rest_framework_simplejwt import views as jwt_views
from .views import CustomUserCreate, ObtainTokenPairWithColorView

urlpatterns = [
    path('user/create/',CustomUserCreate.as_view(),name='create_user'),
    path('token/obtain/',ObtainTokenPairWithColorView.as_view(),name='token_create'),
    path('token/refresh/',jwt_views.TokenRefreshView.as_view(),name='token_refresh'),
]

