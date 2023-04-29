from django.core.management import BaseCommand
from vacancy.typesense_helpers import VacancyTypeSense


class Command(BaseCommand):
    help = "Create vacancy collection"

    def handle(self, *args, **options):
        VacancyTypeSense.create_collection()
