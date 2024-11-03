from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjetViewSet, SprintViewSet, TacheViewSet, RoleViewSet, ProfilUtilisateurViewSet, CommentaireViewSet

# Créer un routeur par défaut
router = DefaultRouter()

# Enregistrer chaque ViewSet avec le routeur
router.register(r'projets', ProjetViewSet)
router.register(r'sprints', SprintViewSet)
router.register(r'taches', TacheViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'profils', ProfilUtilisateurViewSet)
router.register(r'commentaires', CommentaireViewSet)

# Inclure le routeur dans les URL patterns
urlpatterns = [
    path('', include(router.urls)),
]
