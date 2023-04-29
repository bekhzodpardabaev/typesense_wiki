from django.core.management import BaseCommand
from vacancy.typesense_helpers import VacancyTypeSense
import json


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('response.json', 'w') as f:
            json.dump(
                VacancyTypeSense.collection.documents.search({
                    'q': '*',
                    'query_by': 'title',
                    'sort_by': 'published_at:desc',
                    'per_page': 10,
                    'page': 1,
                })
                , f, indent=4)
