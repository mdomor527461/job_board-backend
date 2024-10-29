from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from . import serializers
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import redirect
from rest_framework.permissions import AllowAny
import requests
from rest_framework.response import Response
from rest_framework import status
IMAGEBB_API_KEY = 'bd168c98953ad999e53d8ca206d477fa'
class UserCreateView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request):
        # প্রথমে সিরিয়ালাইজার থেকে ডাটা গ্রহণ করা
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            # যদি ফাইল থাকে তবে ImageBB তে আপলোড করা হবে
            image_file = request.FILES.get('image', None)
            if image_file:
                url = "https://api.imgbb.com/1/upload"
                files = {
                    'image': image_file,
                }
                data = {
                    'key': IMAGEBB_API_KEY,
                }

                # API তে রিকুয়েস্ট পাঠানো
                response = requests.post(url, data=data, files=files)

                # যদি রিকুয়েস্ট সফল হয় তাহলে image_url আপডেট করা
                if response.status_code == 200:
                    image_url = response.json()['data']['url']
                    user.image_url = image_url
                    user.save()

            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# class CustomAuthToken(ObtainAuthToken):

#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data,
#                                            context={'request': request})
#         if serializer.is_valid():
#             user = serializer.validated_data['user']
#             token, created = Token.objects.get_or_create(user=user)
#             return Response({
#                 'token': token.key,
#                 'user_id': user.pk,
#                 'email': user.email
#             })
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginApiView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        # Check if the content type is JSON or Form Data
        if request.content_type == 'application/json':
            data = request.data
        else:  # If it's form data
            data = request.POST

        serializer = serializers.UserLoginSerializer(data=data)
        
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username=username, password=password)
            
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                login(request, user)
                return Response({'token': token.key, 'user_id': user.id,'user_type': user.user_type,'image_url':user.image_url})
            else:
                return Response({'error': "Invalid Credential"}, status=400)
        
        return Response(serializer.errors, status=400)
    
class UserLogoutView(APIView):
    def post(self, request):
        # request.user.auth_token.delete()  # If you're using token authentication
        logout(request)
        return Response({"detail": "Logged out successfully"}, status=200)

class UserListApiView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        id = self.request.query_params.get('id',None)
        if id is not None:
            return User.objects.filter(id = id)
        return User.objects.all()


        