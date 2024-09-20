from rest_framework.serializers import ModelSerializer
from app_livros.models import Livros

class LivrosSerializer(ModelSerializer):
    class Meta:
        model = Livros
        fields = "__all__"