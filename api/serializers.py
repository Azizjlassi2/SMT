from rest_framework import serializers
from .models import *   
from django.contrib.auth.models import User



class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'nom', 'description']


class ProfilUtilisateurSerializer(serializers.ModelSerializer):
    roles = RoleSerializer(many=True, read_only=True)

    class Meta:
        model = ProfilUtilisateur
        fields = ['id', 'utilisateur', 'roles', 'bio']

class ProjetSerializer(serializers.ModelSerializer):
    chef_de_projet = serializers.StringRelatedField()  # Affiche le nom du chef de projet

    class Meta:
        model = Projet
        fields = ['id', 'nom', 'description', 'date_debut', 'date_fin', 'chef_de_projet', 'progression']

class SprintSerializer(serializers.ModelSerializer):
    projet = serializers.StringRelatedField()  # Affiche le nom du projet

    class Meta:
        model = Sprint
        fields = ['id', 'nom', 'projet', 'date_debut', 'date_fin', 'objectif', 'progression']

class TacheSerializer(serializers.ModelSerializer):
    sprint = serializers.StringRelatedField()  # Affiche le nom du sprint
    projet = serializers.StringRelatedField()  # Affiche le nom du projet
    assignation = serializers.StringRelatedField()  # Affiche le nom de l'utilisateur assigné

    class Meta:
        model = Tache
        fields = ['id', 'nom', 'description', 'sprint', 'projet', 'assignation', 'etat', 'priorite', 'date_echeance', 'est_en_retard']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class CommentaireSerializer(serializers.ModelSerializer):
    auteur = serializers.StringRelatedField()  # Affiche le nom de l'auteur (username)
    tache = serializers.StringRelatedField()   # Affiche le nom de la tâche

    class Meta:
        model = Commentaire
        fields = ['id', 'auteur', 'tache', 'contenu', 'date_creation']
        read_only_fields = ['date_creation']  # La date de création est définie automatiquement