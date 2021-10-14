from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import CustomUser

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    In Python, the @classmethod decorator is used to declare a method in the class as a class method that can be called using ClassName.MethodName(). The class method can also be called using an object of the class.

    The first parameter must be cls, which can be used to access class attributes.
    """
    @classmethod
    def get_token(cls,user):
        """  super():
         it allows you to call methods of the superclass in your subclass. The primary use case of this is to extend the functionality of the inherited method.

         lass Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

class Cube(Square):
    def surface_area(self):
        face_area = super().area()
        return face_area * 6

    def volume(self):
        face_area = super().area()
        return face_area * self.length
        """
        token = super(MyTokenObtainPairSerializer,cls).get_token(user)

        token['fav_color'] = user.fav_color
        return token


class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField()
    password = serializers.CharField(min_length=8,write_only=True)


    def create(self,validated_data):
        """ 
            pop method removes the last element or the specified element in a list and returns it.

         """
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = CustomUser
        fields = ('email','username','password')
        extra_kwargs = {'password':{'write_only':True}}

        
    