from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework_jwt.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from .models import *


class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        # fields = '__all__'
        exclude = ['user', 'deleted']
        read_only_fields = ['created_at', 'updated_at', 'deleted_at']
        # fields = ['url', 'id', 'user', 'nom', 'prenom', 'addresse','email', 'contact', 'age', 'genre', 'profil', 'image']


class UserSerializer(serializers.ModelSerializer):
    profile = UtilisateurSerializer(required=False, allow_null=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'password', 'profile']
        extra_kwargs = {
            'password': {'write_only': True},
            'url': {'read_only': True},
        }

    def create(self, validated_data):
        prof_data = validated_data.pop('profile')
        user = User(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        for prof in prof_data:
            Utilisateur.objects.create(user=user, **prof)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        # Unless the application properly enforces that this field is
        # always set, the follow could raise a `DoesNotExist`, which
        # would need to be handled.
        profile = instance.profile

        instance.username = validated_data.get('username', instance.username)
        instance.set_password(validated_data.get(
            'password', instance.password))
        instance.save()

        profile.nom = profile_data.get('nom', profile.nom)
        profile.prenom = profile_data.get('prenom', profile.prenom)
        profile.contact = profile_data.get('contact', profile.contact)
        profile.age = profile_data.get('age', profile.age)
        profile.genre = profile_data.get('genre', profile.genre)
        profile.profil = profile_data.get('profil', profile.profil)
        profile.image = profile_data.get('image', profile.image)
        profile.save()

        return instance

# zone-client start


class ClientSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Client
        # fields = ['url', 'id', 'zoneClt', 'nom', 'prenom', 'dateAdhesion', 'dateNaissance', 'lieuNaissance','sexe', 'contact', 'adresse', 'profession', 'email']
        exclude = ['deleted']
        read_only_fields = ['created_at', 'updated_at', 'deleted_at']


class ZoneSerilizer(serializers.ModelSerializer):
    client_set = ClientSerilizer(read_only=True, many=True)

    class Meta:
        model = Zone
        # fields = ['url', 'id', 'code', 'libelle', 'client']
        # fields = '__all__'
        exclude = ['deleted']
        read_only_fields = ['created_at', 'updated_at', 'deleted_at']
# zine-client end

# compte start


class EpargneSerializer(serializers.ModelSerializer):
    # newClient = ClientSerilizer(required=False, allow_null=True)
    class Meta:
        model = Epargne
        fields = ['url', 'id', 'numero', 'clientEp', 'typeCompte', 'bloque', 'dateLimiteBlocage',
                  'droitAdhsion', 'partSocial', 'soldeInitial', 'soldeBloqué', 'solde']  # , 'newClient']
        extra_kwargs = {
            'soldeInitial': {'write_only': True},
            'soldeBloqué': {'write_only': True},
            'solde': {'write_only': True},
            'dateLimiteBlocage': {'write_only': True},
            # 'newClient': {'write_only': True},
        }

    # def create(self, validated_data):
    #     clt_data = validated_data.pop('newClient')
    #     epargne = Epargne.objects.create(**validated_data)
    #     for clt in clt_data:
    #         Client.objects.create(**clt)
    #     return epargne

    # def update(self, instance, validated_data):
    #     clt_data = validated_data.pop('newClient')
    #     # Unless the application properly enforces that this field is
    #     # always set, the follow could raise a `DoesNotExist`, which
    #     # would need to be handled.
    #     newClient = instance.newClient

    #     instance.username = validated_data.get('username', instance.username)
    #     instance.set_password(validated_data.get(
    #         'password', instance.password))
    #     instance.save()

    #     newClient.nom = clt_data.get('nom', newClient.nom)
    #     newClient.prenom = clt_data.get('prenom', newClient.prenom)
    #     newClient.contact = clt_data.get('contact', newClient.contact)
    #     newClient.age = clt_data.get('age', newClient.age)
    #     newClient.genre = clt_data.get('genre', newClient.genre)
    #     newClient.profil = clt_data.get('profil', newClient.profil)
    #     newClient.image = clt_data.get('image', newClient.image)
    #     newClient.save()

    #     return instance


class MoisSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoisCotisation
        # fields = ['url', 'id', 'compteTontine', 'mise', 'dateDebut', 'dateFin']
        exclude = ['deleted']
        read_only_fields = ['created_at', 'updated_at', 'deleted_at']
        extra_kwargs = {
            'montantMax': {'write_only': True},
            'montantActuel': {'write_only': True},
        }


class TontineSerializer(serializers.ModelSerializer):
    moisCot = MoisSerializer(read_only=True, many=True)

    class Meta:
        model = Tontine
        # fields = ['url', 'id', 'numero', 'clientTont', 'miseActuelle', 'moisCot']
        exclude = ['deleted']
        read_only_fields = ['created_at', 'updated_at', 'deleted_at']
        extra_kwargs = {
            'miseProchaine': {'write_only': True},
            'solde': {'write_only': True},
        }

    # def create(self, validated_data):
    #     moi = validated_data.pop('moisCot')
    #     tontine = Tontine.objects.create(**validated_data)
    #     for m in moi:
    #         MoisCotisation.objects.create(compteTontine=tontine, **moi)
    #     return tontine

    # def update(self, instance, validated_data):
    #     mois = validated_data.pop('moisCot')
    #     moisCot = instance.moisCot

    #     instance.numero = validated_data.get('numero', instance.numero)
    #     instance.clientTont = validated_data.get('clientTont', instance.clientTont)
    #     instance.miseActuelle = validated_data.get('miseActuelle', instance.miseActuelle)
    #     instance.miseProchaine = validated_data.get('miseProchaine', instance.miseProchaine)
    #     instance.solde = validated_data.get('solde', instance.solde)
    #     instance.save()

    #     moisCot.compteTontine = mois.get('compteTontine', moisCot.compteTontine)
    #     moisCot.mise = mois.get('mise', moisCot.mise)
    #     moisCot.dateDebut = mois.get('dateDebut', moisCot.dateDebut)
    #     moisCot.dateFin = mois.get('dateFin', moisCot.dateFin)
    #     moisCot.montantMax = mois.get('montantMax', moisCot.montantMax)
    #     moisCot.montantActuel = mois.get('montantActuel', moisCot.montantActuel)
    #     moisCot.save()

    #     return instance

# compte end


class Mois(serializers.ModelSerializer):
    class Meta:
        model = MoisCotisation
        # fields = ['url', 'id', 'zoneClt', 'nom', 'prenom', 'dateAdhesion', 'dateNaissance', 'lieuNaissance','sexe', 'contact', 'adresse', 'profession', 'email']
        exclude = ['deleted']
        read_only_fields = ['created_at', 'updated_at', 'deleted_at']


class Tont(serializers.ModelSerializer):
    mois_Cotisation_set = MoisSerializer(required=False, many=True)

    class Meta:
        model = Tontine
        # fields = ['url', 'id', 'code', 'libelle', 'client']
        # fields = '__all__'
        exclude = ['deleted']
        read_only_fields = ['created_at', 'updated_at', 'deleted_at']

class TypeCreditEpatrgneSerilaizer(serializers.ModelSerializer):
    mois_Cotisation_set = MoisSerializer(required=False, many=True)

    class Meta:
        model = TypeCreditEpargne
        exclude = ['deleted']
        read_only_fields = ['created_at', 'updated_at', 'deleted_at']


class TypeCreditTontineSerializer(serializers.ModelSerializer):
    mois_Cotisation_set = MoisSerializer(required=False, many=True)

    class Meta:
        model = TypeCreditTontine
        exclude = ['deleted']
        read_only_fields = ['created_at', 'updated_at', 'deleted_at']
