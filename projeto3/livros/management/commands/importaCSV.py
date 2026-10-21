import csv
from django.core.management.base import BaseCommand
from livros.models import Autor, Livro


class Command(BaseCommand):
    help = 'Importa livros de um arquivo CSV'

    def add_arguments(self, parser):
        parser.add_argument('base_livros', type=str)

    def handle(self, *args, **kwargs):
        with open(kwargs['base_livros'], newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                autor_nome = row['autor']
                autor, _ = Autor.objects.get_or_create(nome=autor_nome)
                Livro.objects.get_or_create(
                    titulo=row['titulo'],
                    autor=autor,
                    isbn=row['isbn'],
                    paginas=int(row['paginas']),
                    ano=int(row['ano_publicacao'])
                )

        self.stdout.write(self.style.SUCCESS('Importação concluída!'))