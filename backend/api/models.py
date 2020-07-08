from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
import uuid
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils import timezone


# Create your models here.


class TimeVirtualModel(models.Model):
    created_at = models.DateTimeField("Date creation", auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField("Date de mise ajour", auto_now=True, blank=True, null=True)
    deleted = models.BooleanField(default=False, blank=True, null=True)
    deleted_at = models.DateTimeField("Date de suppression", blank=True, null=True)

    def __suppress__(self):
        self.deleted = True
        self.deleted_at = timezone.now

    def __restore__(self):
        self.deleted = False
        self.deleted_at = None

    def __str__(self):
        return self.id


# class User(Abstr)
class Utilisateur(TimeVirtualModel):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile', blank=True, null=True)
    nom = models.CharField(max_length=50, blank=True, null=True)
    prenom = models.CharField(max_length=50, blank=True, null=True)
    addresse = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField(
        max_length=254, unique=True, blank=True, null=True)
    contact = models.CharField(
        max_length=10, unique=True, null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    CHOIX_GENRE = (
        ('M', 'Masculin'),
        ('F', 'Feminin'),
    )
    genre = models.CharField(
        max_length=1, choices=CHOIX_GENRE, blank=True, null=True)
    CHOIX_PROFIL = (
        ('AGT', 'Agent de Terrain'),
        ('SEC', 'Secretaire'),
        ('CAS', 'Caissier'),
        ('CPT', 'Comptable'),
        ('CTL', 'Controleur'),
    )
    profil = models.CharField(
        max_length=5, choices=CHOIX_PROFIL, blank=True, null=True)
    image = models.ImageField(
        upload_to="User/Profile", blank=True, null=True, verbose_name="Image de profile")

    def __str__(self):
        return self.nom


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = Utilisateur.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)
# class User(Abstr)


class CompteComptable(TimeVirtualModel):
    createur = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, blank=True, null=True)
    code = models.CharField(max_length=50, blank=True, null=True)
    numero = models.CharField(max_length=50, blank=True, null=True)
    groupe = models.CharField(max_length=50, blank=True, null=True)
    classe = models.IntegerField(blank=True, null=True)
    statut = models.CharField(max_length=50, blank=True, null=True)
    montantStatut = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.numero


class Operation (TimeVirtualModel):
    operateur = models.ForeignKey(
        User, related_name="Operateur", on_delete=models.DO_NOTHING, blank=True, null=True)
    date = models.DateField("Date de l'operation", blank=True, null=True)
    CHOIX_OPER = (
        ('DEP', 'Depot'),
        ('RET', 'Retrait'),
    )
    typeOperationp = models.CharField(
        max_length=5, choices=CHOIX_OPER, blank=True, null=True)
    libelle = models.CharField(max_length=50)
    montant = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.typeOperationp}-{self.id}"


class Alimentation(TimeVirtualModel):
    caissier = models.ForeignKey(
        User, related_name='Caissier', on_delete=models.CASCADE, blank=True, null=True)
    agent = models.ForeignKey(
        User, related_name='Agent', on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField(auto_now=True)
    montant = models.FloatField(blank=True, null=True)
    nbrb10000 = models.IntegerField(
        "Nombre de billets de 10.000F", blank=True, null=True)
    nbrb5000 = models.IntegerField(
        "Nombre de billets de 5.000F", blank=True, null=True)
    nbrb2000 = models.IntegerField(
        "Nombre de billets de 2.000F", blank=True, null=True)
    nbrb1000 = models.IntegerField(
        "Nombre de billets de 1.000F", blank=True, null=True)
    nbrb500 = models.IntegerField(
        "Nombre de billets de 500F", blank=True, null=True)
    nbrp500 = models.IntegerField(
        "Nombre de pieces de 500F", blank=True, null=True)
    nbrp250 = models.IntegerField(
        "Nombre de pieces de 250F", blank=True, null=True)
    nbrp200 = models.IntegerField(
        "Nombre de pieces de 200F", blank=True, null=True)
    nbrp100 = models.IntegerField(
        "Nombre de pieces de 100F", blank=True, null=True)
    nbrp50 = models.IntegerField(
        "Nombre de pieces de 50F", blank=True, null=True)
    nbrp25 = models.IntegerField(
        "Nombre de pieces de 25F", blank=True, null=True)
    nbrp10 = models.IntegerField(
        "Nombre de pieces de 10F", blank=True, null=True)
    nbrp5 = models.IntegerField(
        "Nombre de pieces de 5F", blank=True, null=True)

    def __str__(self):
        return f"{self.id}"


class Zone(TimeVirtualModel):
    code = models.CharField(max_length=50, blank=True, null=True)
    libelle = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.code


class Client(TimeVirtualModel):
    zoneClt = models.ForeignKey(
        Zone, verbose_name='zone', on_delete=models.DO_NOTHING, blank=True, null=True)
    nom = models.CharField(max_length=50, blank=True, null=True)
    prenom = models.CharField(max_length=80, blank=True, null=True)
    dateAdhesion = models.DateField(auto_now=True, blank=True, null=True)
    dateNaissance = models.DateField(blank=True, null=True)
    lieuNaissance = models.CharField(max_length=150, blank=True, null=True)
    sexe = models.CharField(max_length=10, blank=True, null=True)
    contact = models.CharField(max_length=20, blank=True, null=True)
    adresse = models.CharField(max_length=150, blank=True, null=True)
    profession = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.nom


class Epargne(TimeVirtualModel):
    numero = models.CharField(max_length=50, blank=True, null=True)
    clientEp = models.ForeignKey(
        Client, on_delete=models.CASCADE, blank=True, null=True)
    CHOIX_TYPE = (
        ('PHY', 'Physique'),
        ('MOR', 'Morale'),
    )
    typeCompte = models.CharField(
        max_length=5, choices=CHOIX_TYPE, default='PHY', blank=True, null=True)
    dateCreation = models.DateField(auto_now_add=True, blank=True, null=True)
    bloque = models.BooleanField(default=None, blank=True, null=True)
    dateLimiteBlocage = models.DateField(blank=True, null=True)
    droitAdhsion = models.FloatField(blank=True, null=True)
    partSocial = models.FloatField(blank=True, null=True)
    soldeInitial = models.FloatField(blank=True, null=True)
    soldeBloqué = models.FloatField(blank=True, null=True)
    solde = models.FloatField(default=0, blank=True, null=True)

    def __str__(self):
        return f"{self.typeCompte}-{self.id}"


class DepotEpargne(TimeVirtualModel):
    date = models.DateField(auto_now_add=True, blank=True, null=True)
    deposeur = models.CharField(max_length=50, blank=True, null=True)
    montant = models.FloatField(blank=True, null=True)
    nouveau_solde = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"Depot de {self.montant}F"


class RetraitEpargne(TimeVirtualModel):
    date = models.DateField(auto_now_add=True, blank=True, null=True)
    receveur = models.CharField(max_length=50, blank=True, null=True)
    montant = models.FloatField(blank=True, null=True)
    nouveau_solde = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"Retrait de {self.montant}F"


class Mouvement(TimeVirtualModel):
    retrait = models.ForeignKey(
        RetraitEpargne, on_delete=models.CASCADE, blank=True, null=True)
    depot = models.ForeignKey(
        DepotEpargne, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    libelle = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.id}"


def create_mouvement_depot(sender, **kwargs):
    if kwargs['created']:
        depot_mouvement = Mouvement.objects.create(depot=kwargs['instance'])


post_save.connect(create_mouvement_depot, sender=DepotEpargne)


def create_mouvement_retrait(sender, **kwargs):
    if kwargs['created']:
        retrait_mouvement = Mouvement.objects.create(
            retrait=kwargs['instance'])


post_save.connect(create_mouvement_retrait, sender=RetraitEpargne)


class Tontine(TimeVirtualModel):
    numero = models.CharField(max_length=50, blank=True, null=True)
    clientTont = models.ForeignKey(
        Client, on_delete=models.CASCADE, blank=True, null=True)
    dateCreation = models.DateField(auto_now_add=True, blank=True, null=True)
    miseActuelle = models.FloatField(blank=True, null=True)
    miseProchaine = models.FloatField(blank=True, null=True)
    solde = models.FloatField(default=0, blank=True, null=True)

    def __str__(self):
        return f"{self.clientTont} - {self.id}"


class MoisCotisation(TimeVirtualModel):
    compteTontine = models.ForeignKey(
        Tontine, on_delete=models.DO_NOTHING, blank=True, null=True)
    mise = models.FloatField(blank=True, null=True)
    dateDebut = models.DateField(blank=True, null=True)
    dateFin = models.DateField(blank=True, null=True)
    montantMax = models.FloatField(blank=True, null=True)
    montantActuel = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.id}"


class Cotisation(TimeVirtualModel):
    mois = models.ForeignKey(
        MoisCotisation, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField(auto_now_add=True, blank=True, null=True)
    montant = models.FloatField(blank=True, null=True)
    montant = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.typeOperationp} - {self.id}"


class Commission(TimeVirtualModel):
    agent = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, blank=True, null=True)
    CpTontine = models.ForeignKey(
        Tontine, on_delete=models.DO_NOTHING, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    montant = models.FloatField(blank=True, null=True)


class RetraitTontine(TimeVirtualModel):
    compteTontine = models.ForeignKey(
        Tontine, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField(auto_now_add=True, blank=True, null=True)
    montant = models.FloatField(blank=True, null=True)
    nouveauSolde = models.FloatField(blank=True, null=True)


class TypeCreditEpargne(TimeVirtualModel):
    libelle = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.libelle


class TypeCreditTontine(TimeVirtualModel):
    libelle = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.libelle


class CreditTontine(TimeVirtualModel):
    agent_de_credit = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.ForeignKey(TypeCreditEpargne, verbose_name="Type credit Epargne",
                             on_delete=models.SET_NULL, blank=True, null=True)
    compte_tontine = models.ForeignKey(
        Tontine, verbose_name="Compte Tontine", on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField(auto_now_add=True, blank=True, null=True)
    numero = models.CharField(max_length=50, blank=True, null=True)
    nature_taux = models.CharField(blank=True, null=True, max_length=50)
    taux_interet = models.FloatField(blank=True, null=True)
    frais_dossier = models.FloatField(blank=True, null=True)
    frais_gestion = models.FloatField(blank=True, null=True)
    frais_assurance = models.FloatField(blank=True, null=True)
    nbe_echeances = models.IntegerField(
        "nombre d'escheances", blank=True, null=True)
    duree_echeance = models.CharField(
        "Année/Mois/Jours", max_length=150, blank=True, null=True)
    nantissement = models.FloatField(blank=True, null=True)
    montant = models.FloatField(blank=True, null=True)
    date_limite = models.DateField(blank=True, null=True)
    montant_rembourse = models.FloatField(
        "somme deja remboursé", blank=True, null=True)
    reste_a_rembourser = models.FloatField(
        "reste à rembourser", blank=True, null=True)
    rembourse = models.NullBooleanField(blank=True, null=True, default=False)
    prochaine_echeance = models.IntegerField(blank=True, null=True)
    montant_prevue = models.FloatField(blank=True, null=True)
    date_prevue = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.numero}"


class RembourssementTontine(TimeVirtualModel):
    credit_tontine = models.ForeignKey(
        CreditTontine, blank=True, null=True, on_delete=models.CASCADE)
    models.DateField(blank=True, null=True, auto_now_add=True)
    montant = models.FloatField(blank=True, null=True)
    interet = models.FloatField(blank=True, null=True)
    penalites = models.FloatField(default=0.0, blank=True, null=True)
    remboursseur = models.CharField(blank=True, null=True, max_length=50)

    def __str__(self):
        return f"Rembourssement Tontine-{self.id}"


class CreditEpargne(TimeVirtualModel):
    agent_de_credit = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.ForeignKey(TypeCreditEpargne, verbose_name="Type credit Epargne",
                             on_delete=models.SET_NULL, blank=True, null=True)
    compte_epargne = models.ForeignKey(
        Epargne, verbose_name="Compte Epargne", on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField(auto_now_add=True, blank=True, null=True)
    numero = models.CharField(max_length=50, blank=True, null=True)
    nature_taux = models.CharField(blank=True, null=True, max_length=50)
    taux_interet = models.FloatField(blank=True, null=True)
    frais_dossier = models.FloatField(blank=True, null=True)
    frais_gestion = models.FloatField(blank=True, null=True)
    frais_assurance = models.FloatField(blank=True, null=True)
    nbe_echeances = models.IntegerField(
        "nombre d'escheances", blank=True, null=True)
    duree_echeance = models.CharField(
        "Année/Mois/Jours", max_length=150, blank=True, null=True)
    nantissement = models.FloatField(blank=True, null=True)
    montant = models.FloatField(blank=True, null=True)
    date_limite = models.DateField(blank=True, null=True)
    montant_rembourse = models.FloatField(
        "somme deja remboursé", blank=True, null=True)
    reste_a_rembourser = models.FloatField(
        "reste à rembourser", blank=True, null=True)
    rembourse = models.NullBooleanField(blank=True, null=True, default=False)
    prochaine_echeance = models.IntegerField(blank=True, null=True)
    montant_prevue = models.FloatField(blank=True, null=True)
    date_prevue = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.numero}"


class RembourssementEpargne(TimeVirtualModel):
    credit_epargne = models.ForeignKey(
        CreditEpargne, blank=True, null=True, on_delete=models.CASCADE)
    models.DateField(blank=True, null=True, auto_now_add=True)
    montant = models.FloatField(blank=True, null=True)
    interet = models.FloatField(blank=True, null=True)
    penalites = models.FloatField(default=0.0, blank=True, null=True)
    remboursseur = models.CharField(blank=True, null=True, max_length=50)

    def __str__(self):
        return f"Rembourssement Epargne-{self.id}"


class Amortissement(TimeVirtualModel):
    credit_epargne = models.ForeignKey(
        CreditEpargne, on_delete=models.CASCADE, blank=True, null=True)
    credit_tontine = models.ForeignKey(
        CreditTontine, on_delete=models.CASCADE, blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    mensualite_due = models.FloatField(blank=True, null=True)
    interet_mensuel_du = models.FloatField(blank=True, null=True)
    capital_mensuel_du = models.FloatField(blank=True, null=True)
    solde_capital_due = models.FloatField(blank=True, null=True)
    solde_mensualite_due = models.FloatField(blank=True, null=True)
    rembourse = models.BooleanField(default=False, blank=True, null=True)
    date_remboursement = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.numero
