from django.shortcuts import render
from .serializers import ArticleSerializer
from .models import Article
from rest_framework import viewsets
from rest_framework.permissions import AllowAny,IsAuthenticated,BasePermission,SAFE_METHODS
#from rest_framework.decorators import api_view,permission_classes

# Create your views here.
#@api_view(['POST'])
#@permission_classes((AllowAny,))
#@csrf_exempt
class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

class ArticleView(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    permission_classes = [IsAuthenticated]
   
