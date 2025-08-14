from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.models import update_last_login
from rest_framework_simplejwt.settings import api_settings

User = get_user_model()

def authenticate_by_email(email, password):
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return None
    if user.check_password(password) and user.is_active:
        return user
    return None

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'email'  # On veut utiliser l'email

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['role'] = user.role
        return token

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if not email or not password:
            raise serializers.ValidationError('Email et mot de passe sont requis.')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError('Utilisateur non trouvé avec cet email.')

        if not user.check_password(password):
            raise serializers.ValidationError('Email ou mot de passe incorrect.')

        if not user.is_active:
            raise serializers.ValidationError('Compte désactivé.')

        # Crée manuellement les tokens
        refresh = self.get_token(user)
        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': {
                'username': user.username,
                'role': user.role,
            }
        }

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, user)

        return data
