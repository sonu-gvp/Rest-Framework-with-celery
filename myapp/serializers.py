from rest_framework import serializers
from myapp.models import Register
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ['id', 'first_name', 'last_name', 'email', 'mobile', 'image']


class UserSerializer(serializers.ModelSerializer):
	"""docstring for UserSerializer"""
	class Meta:
		model = User
		fields = ['id', 'username', 'email', 'password']
			