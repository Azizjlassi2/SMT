from datetime import timezone
from django.db import models
from django.contrib.auth.models import User

class Projet(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    date_debut = models.DateField()
    date_fin = models.DateField(blank=True, null=True)
    chef_de_projet = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projets")

    def __str__(self):
        return self.nom

    def progression(self):
        """Calcul de la progression globale du projet en fonction des tâches terminées."""
        taches = self.taches.all()
        termine = taches.filter(etat='TERMINE').count()
        total = taches.count()
        return (termine / total * 100) if total > 0 else 0


class Sprint(models.Model):
    nom = models.CharField(max_length=100)
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE, related_name="sprints")
    date_debut = models.DateField()
    date_fin = models.DateField()
    objectif = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nom} ({self.projet.nom})"

    def progression(self):
        """Calcul de la progression du sprint en fonction des tâches terminées."""
        taches = self.taches.all()
        termine = taches.filter(etat='TERMINE').count()
        total = taches.count()
        return (termine / total * 100) if total > 0 else 0

class Tache(models.Model):
    ETATS = [
        ('A_FAIRE', 'À faire'),
        ('EN_COURS', 'En cours'),
        ('TERMINE', 'Terminé')
    ]

    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE, related_name="taches")
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE, related_name="taches")
    assignation = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="taches")
    etat = models.CharField(max_length=10, choices=ETATS, default='A_FAIRE')
    priorite = models.IntegerField(default=0)
    date_echeance = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.nom} ({self.sprint.nom})"

    def est_en_retard(self):
        """Vérifie si la tâche est en retard par rapport à la date d'échéance."""
        if self.date_echeance and self.etat != 'TERMINE':
            return self.date_echeance < timezone.now().date()
        return False

class Role(models.Model):
    nom = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nom


class ProfilUtilisateur(models.Model):
    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profil')
    roles = models.ManyToManyField(Role, related_name='utilisateurs')
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.utilisateur.username} - {', '.join(role.nom for role in self.roles.all())}"

    def has_role(self, role_name):
        """Vérifie si l'utilisateur possède un rôle spécifique."""
        return self.roles.filter(nom=role_name).exists()



class Commentaire(models.Model):
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    tache = models.ForeignKey(Tache, on_delete=models.CASCADE, related_name="commentaires")
    contenu = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commentaire de {self.auteur.username} sur {self.tache.nom}"
