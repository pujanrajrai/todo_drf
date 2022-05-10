from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import User


class RegisterSerializers(serializers.ModelSerializer):
    password2 = serializers.CharField(min_length=8, max_length=20)
    password = serializers.CharField(min_length=8, max_length=20)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']

    def validate(self, data):
        error = {}

        username = data['username']
        email = data['email']
        password = data['password']
        password2 = data['password2']

        if password != password2:
            error['password'] = "password and confirm password doesn't match"
        special_sym = ['$', '@', '#', '%']

        # checking if password contains number or not
        if not any(char.isdigit() for char in password):
            error['password_digit'] = 'password must contain at least one Number'

        # checking if password contains uppercase or not
        if not any(char.isupper() for char in password):
            error['password_upper_case'] = 'Password should have at least one uppercase letter'

        # checking if password contains is lower or not
        if not any(char.islower() for char in password):
            error['password_lower_case'] = 'Password should have at least one uppercase letter'

        # checking if password contains special symbol or not
        if not any(char in special_sym for char in password):
            error['password_special_case'] = 'Password should have at least one uppercase letter'

        if error:
            raise serializers.ValidationError(error)

        new_data = {
            'username': username,
            'email': email,
            'password': make_password(password),
        }

        return new_data


