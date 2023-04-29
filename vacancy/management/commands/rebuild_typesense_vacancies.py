import typesense.exceptions
from django.core.management import BaseCommand
from vacancy.typesense_helpers import VacancyTypeSense
from vacancy.models import Vacancy


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            VacancyTypeSense.collection.retrieve()
        except typesense.exceptions.ObjectNotFound:
            print('Creating collection "{}"...'.format(VacancyTypeSense.COLLECTION_NAME))
            VacancyTypeSense.create_collection()
            print('Creating documents...')
            for vacancy in Vacancy.objects.iterator():
                VacancyTypeSense.create_vacancy(vacancy)
        else:
            print('Deleting collection "{}"...'.format(VacancyTypeSense.COLLECTION_NAME))
            VacancyTypeSense.client.collections[VacancyTypeSense.COLLECTION_NAME].delete()
            print('Creating collection "{}"...'.format(VacancyTypeSense.COLLECTION_NAME))
            VacancyTypeSense.create_collection()

            print('Creating documents...')
            for vacancy in Vacancy.objects.iterator():
                VacancyTypeSense.create_vacancy(vacancy)
