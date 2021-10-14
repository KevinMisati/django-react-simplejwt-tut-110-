from rest_framework import routers
from .views import ArticleView
from django.urls import path,include

router = routers.DefaultRouter()                   
router.register('articles', ArticleView, 'todo')  

urlpatterns = [
    path('',include(router.urls))
]