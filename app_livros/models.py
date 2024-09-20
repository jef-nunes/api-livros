from django.db.models import Model, UUIDField, CharField, IntegerField, DateField
from uuid import uuid4
# Create your models here.
class Livros(Model):
    id_livro = UUIDField(primary_key=True, default=uuid4, editable=False)
    titulo = CharField(max_length=255)
    autor = CharField(max_length=255)
    data_lancamento = IntegerField()
    estado = CharField(max_length=50)
    paginas = IntegerField()
    editora = CharField(max_length=255)
    data_registro_bd = DateField(auto_now_add=True)