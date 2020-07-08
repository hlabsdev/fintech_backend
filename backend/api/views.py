from django.shortcuts import render
from django.utils import timezone
from rest_framework import renderers, viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework.reverse import reverse
from .serializers import *


# Ges User start
class UserViewSet(viewsets.ModelViewSet):
    """
    me donne acces aux url 'list' et 'detail' en meme temps
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

# # Methodes suplementaire start
#     def destroy(self, request, pk=None):
#         objet = User.objects.get(pk=pk)
#         try:
#             objet.deleted = True
#             objet.deleted_at = timezone.now()
#             objet.save()
#             return Response({'status': 'Suppression faite'})
#         except:
#             return Response({'status': 'Erreur lors de la suppression'})

#     @action(detail=True, permission_classes=[permissions.IsAuthenticated])
#     def restore(self, request, pk=None):
#         objet = Zone.objects.get(pk=pk)
#         try:
#             objet.deleted = False
#             objet.deleted_at = None
#             objet.save()
#             return Response({'status': 'Les données ont été restaurées avec succes'})
#         except:
#             return Response({'status': 'Erreur lors de la suppression'})

#     @action(detail=False, permission_classes=[permissions.IsAuthenticated])
#     def get_deleted_list(self, request):
#         objet = Zone.objects.filter(deleted=True).order_by('-deleted_at')
#         serializer = self.get_serializer(objet, many=True)
#         return Response(serializer.data)
# # Methodes suplementaire end


class ProfileViewSet(viewsets.ModelViewSet):

    queryset = Utilisateur.objects.filter(deleted=False)
    serializer_class = UtilisateurSerializer
    permission_classes = [permissions.IsAuthenticated]

# Methodes suplementaire start
    def destroy(self, request, pk=None):
        objet = Utilisateur.objects.get(pk=pk)
        try:
            objet.deleted = True
            objet.deleted_at = timezone.now()
            objet.save()
            return Response({'status': 'Suppression faite'})
        except:
            return Response({'status': 'Erreur lors de la suppression'})

    @action(detail=True, permission_classes=[permissions.IsAuthenticated])
    def restore(self, request, pk=None):
        objet = Utilisateur.objects.get(pk=pk)
        try:
            objet.deleted = False
            objet.deleted_at = None
            objet.save()
            return Response({'status': 'Les données ont été restaurées avec succes'})
        except:
            return Response({'status': 'Erreur lors de la suppression'})

    @action(detail=False, permission_classes=[permissions.IsAuthenticated])
    def get_deleted_list(self, request):
        objet = Utilisateur.objects.filter(deleted=True).order_by('-deleted_at')
        serializer = self.get_serializer(objet, many=True)
        return Response(serializer.data)
# Methodes suplementaire end

# Ges User end

# Zone client start



class ZoneSet(viewsets.ModelViewSet):
    # queryset = Zone.objects.all()
    queryset = Zone.objects.filter(deleted=False)
    serializer_class = ZoneSerilizer
    permission_classes = [permissions.IsAuthenticated]
    
# Methodes suplementaire start

    def destroy(self, request, pk=None):
        objet = Zone.objects.get(pk=pk)
        try:
            objet.deleted = True
            objet.deleted_at = timezone.now()
            objet.save()
            return Response({'status': 'Suppression faite'})
        except:
            return Response({'status': 'Erreur lors de la suppression'})

    @action(detail=True, permission_classes=[permissions.IsAuthenticated])
    def restore(self, request, pk=None):
        objet = Zone.objects.get(pk=pk) 
        try:
            objet.deleted = False
            objet.deleted_at = None
            objet.save()
            return Response({'status': 'Les données ont été restaurées avec succes'})
        except:
            return Response({'status': 'Erreur lors de la suppression'})

    @action(detail=False, permission_classes=[permissions.IsAuthenticated])
    def get_deleted_list(self, request):
        objet = Zone.objects.filter(deleted=True).order_by('-deleted_at')
        serializer = self.get_serializer(objet, many=True)
        return Response(serializer.data)
# Methodes suplementaire endet


class ClientSet(viewsets.ModelViewSet):
    queryset = Client.objects.filter(deleted=False)
    serializer_class = ClientSerilizer
    permission_classes = [permissions.IsAuthenticated]

# Methodes suplementaire start
    def destroy(self, request, pk=None):
        objet = Client.objects.get(pk=pk)
        try:
            objet.deleted = True
            objet.deleted_at = timezone.now()
            objet.save()
            return Response({'status': 'Suppression faite'})
        except:
            return Response({'status': 'Erreur lors de la suppression'})

    @action(detail=True, permission_classes=[permissions.IsAuthenticated])
    def restore(self, request, pk=None):
        objet = Client.objects.get(pk=pk)
        try:
            objet.deleted = False
            objet.deleted_at = None
            objet.save()
            return Response({'status': 'Les données ont été restaurées avec succes'})
        except:
            return Response({'status': 'Erreur lors de la suppression'})

    @action(detail=False, permission_classes=[permissions.IsAuthenticated])
    def get_deleted_list(self, request):
        objet = Client.objects.filter(deleted=True).order_by('-deleted_at')
        serializer = self.get_serializer(objet, many=True)
        return Response(serializer.data)
# Methodes suplementaire end

# Epargne client end

# Comptes start


class EpargneSet(viewsets.ModelViewSet):
    queryset = Epargne.objects.filter(deleted=False)
    serializer_class = EpargneSerializer
    permission_classes = [permissions.IsAuthenticated]

# Methodes suplementaire start
    def destroy(self, request, pk=None):
        objet = Epargne.objects.get(pk=pk)
        try:
            objet.deleted = True
            objet.deleted_at = timezone.now()
            objet.save()
            return Response({'status': 'Suppression faite'})
        except:
            return Response({'status': 'Erreur lors de la suppression'})

    @action(detail=True, permission_classes=[permissions.IsAuthenticated])
    def restore(self, request, pk=None):
        objet = Epargne.objects.get(pk=pk)
        try:
            objet.deleted = False
            objet.deleted_at = None
            objet.save()
            return Response({'status': 'Les données ont été restaurées avec succes'})
        except:
            return Response({'status': 'Erreur lors de la suppression'})

    @action(detail=False, permission_classes=[permissions.IsAuthenticated])
    def get_deleted_list(self, request):
        objet = Epargne.objects.filter(deleted=True).order_by('-deleted_at')
        serializer = self.get_serializer(objet, many=True)
        return Response(serializer.data)
# Methodes suplementaire end



class TontineSet(viewsets.ModelViewSet):
    queryset = Tontine.objects.filter(deleted=False)
    serializer_class = Tont
    permission_classes = [permissions.IsAuthenticated]

# Methodes suplementaire start
    def destroy(self, request, pk=None):
        objet = Tontine.objects.get(pk=pk)
        try:
            objet.deleted = True
            objet.deleted_at = timezone.now()
            objet.save()
            return Response({'status': 'Suppression faite'})
        except:
            return Response({'status': 'Erreur lors de la suppression'})

    @action(detail=True, permission_classes=[permissions.IsAuthenticated])
    def restore(self, request, pk=None):
        objet = Tontine.objects.get(pk=pk)
        try:
            objet.deleted = False
            objet.deleted_at = None
            objet.save()
            return Response({'status': 'Les données ont été restaurées avec succes'})
        except:
            return Response({'status': 'Erreur lors de la suppression'})

    @action(detail=False, permission_classes=[permissions.IsAuthenticated])
    def get_deleted_list(self, request):
        objet = Tontine.objects.filter(deleted=True).order_by('-deleted_at')
        serializer = self.get_serializer(objet, many=True)
        return Response(serializer.data)
# Methodes suplementaire end

# Comptes end


# Cotisation start

class MoisCotiseSet(viewsets.ModelViewSet):
    queryset = MoisCotisation.objects.filter(deleted=False)
    serializer_class = Mois
    permission_classes = [permissions.IsAuthenticated]

# Methodes suplementaire start
    def destroy(self, request, pk=None):
        objet = MoisCotisation.objects.get(pk=pk)
        try:
            objet.deleted = True
            objet.deleted_at = timezone.now()
            objet.save()
            return Response({'status': 'Suppression faite'})
        except:
            return Response({'status': 'Erreur lors de la suppression'})

    @action(detail=True, permission_classes=[permissions.IsAuthenticated])
    def restore(self, request, pk=None):
        objet = MoisCotisation.objects.get(pk=pk)
        try:
            objet.deleted = False
            objet.deleted_at = None
            objet.save()
            return Response({'status': 'Les données ont été restaurées avec succes'})
        except:
            return Response({'status': 'Erreur lors de la suppression'})

    @action(detail=False, permission_classes=[permissions.IsAuthenticated])
    def get_deleted_list(self, request):
        objet = MoisCotisation.objects.filter(deleted=True).order_by('-deleted_at')
        serializer = self.get_serializer(objet, many=True)
        return Response(serializer.data)
# Methodes suplementaire end

# Cotisation end =============================================

# Type Credit Epargne start

class TypeCreditEpargneSet(viewsets.ModelViewSet):
    queryset = TypeCreditEpargne.objects.filter(deleted=False)
    serializer_class = TypeCreditEpatrgneSerilaizer
    permission_classes = [permissions.IsAuthenticated]

# Methodes suplementaire start
    def destroy(self, request, pk=None):
        objet = TypeCreditEpargne.objects.get(pk=pk)
        try:
            objet.deleted = True
            objet.deleted_at = timezone.now()
            objet.save()
            return Response({'status': 'Suppression faite'})
        except:
            return Response({'status': 'Erreur lors de la suppression'})

    @action(detail=True, permission_classes=[permissions.IsAuthenticated])
    def restore(self, request, pk=None):
        objet = TypeCreditEpargne.objects.get(pk=pk)
        try:
            objet.deleted = False
            objet.deleted_at = None
            objet.save()
            return Response({'status': 'Les données ont été restaurées avec succes'})
        except:
            return Response({'status': 'Erreur lors de la suppression'})

    @action(detail=False, permission_classes=[permissions.IsAuthenticated])
    def get_deleted_list(self, request):
        objet = TypeCreditEpargne.objects.filter(deleted=True).order_by('-deleted_at')
        serializer = self.get_serializer(objet, many=True)
        return Response(serializer.data)
# Methodes suplementaire end

# Type Credit Epargne end =============================================



# Type Credit Tontine start

class TypeCreditTontineSet(viewsets.ModelViewSet):
    queryset = TypeCreditTontine.objects.filter(deleted=False)
    serializer_class = TypeCreditTontineSerializer
    permission_classes = [permissions.IsAuthenticated]

# Methodes suplementaire start
    def destroy(self, request, pk=None):
        objet = TypeCreditTontine.objects.get(pk=pk)
        try:
            objet.deleted = True
            objet.deleted_at = timezone.now()
            objet.save()
            return Response({'status': 'Suppression faite'})
        except:
            return Response({'status': 'Erreur lors de la suppression'})

    @action(detail=True, permission_classes=[permissions.IsAuthenticated])
    def restore(self, request, pk=None):
        objet = TypeCreditTontine.objects.get(pk=pk)
        try:
            objet.deleted = False
            objet.deleted_at = None
            objet.save()
            return Response({'status': 'Les données ont été restaurées avec succes'})
        except:
            return Response({'status': 'Erreur lors de la suppression'})

    @action(detail=False, permission_classes=[permissions.IsAuthenticated])
    def get_deleted_list(self, request):
        objet = TypeCreditTontine.objects.filter(deleted=True).order_by('-deleted_at')
        serializer = self.get_serializer(objet, many=True)
        return Response(serializer.data)
# Methodes suplementaire end

# Type Credit Tontine end =============================================



# Api root
# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'get_token': reverse('get_token', request=request, format=format),
#         # 'auth': reverse('get_token', request=request, format=format),
#     })
