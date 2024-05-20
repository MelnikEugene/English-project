from django.core.management.base import BaseCommand
from tasks.models import Word

class Command(BaseCommand):
    help = 'Populates the database with predefined words'

    def handle(self, *args, **options):
        words = [
            ('ты', 'you'),
            ('они', 'they')
        ]

        for russian, english in words:
            Word.objects.create(russian=russian, english=english)

        self.stdout.write(self.style.SUCCESS('Successfully populated words'))

