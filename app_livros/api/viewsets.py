from rest_framework.viewsets import ModelViewSet
from app_livros.api.serializers import LivrosSerializer
from app_livros.models import Livros

class LivrosViewSet(ModelViewSet):
    serializer_class = LivrosSerializer
    queryset = Livros.objects.all()
