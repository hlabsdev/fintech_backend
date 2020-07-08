from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework_jwt.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from api.models import *

class UtilisateurSerializer(serializers.ModelSerializer):
    profile = Utilisateur()
    class Meta:
        model=User
        fields = '__all__'

class CompteComptableSerializer(serializers.ModelSerializer):
    class Meta:
        model=CompteComptable
        fields = '__all__'