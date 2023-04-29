import json
from django.db.models import Case, When
from rest_framework.filters import SearchFilter
from vacancy.typesense_helpers import VacancyTypeSense


class TypesenseSearchFilterBackend(SearchFilter):

    def get_typesense_search_schema(self, view):
        return getattr(view, 'typesense_search_schema')

    def filter_queryset(self, request, queryset, view):
        search_query = "".join(self.get_search_terms(request))
        if not search_query:
            return queryset.none()
        print(search_query)

        typesense_search_schema = self.get_typesense_search_schema(view)
        typesense_search_schema.update({'q': search_query})

        results = VacancyTypeSense.collection.documents.search(typesense_search_schema)

        with open("response.json", "w") as f:
            json.dump(results, f, indent=4)

        return self.typesense_to_queryset([hit['document'] for hit in results['hits']], queryset)

    def typesense_to_queryset(self, docs_list, queryset):
        pk_list = [doc['id'] for doc in docs_list]
        qs = queryset.filter(pk__in=pk_list)

        preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(pk_list)])
        return qs.filter(pk__in=pk_list).order_by(preserved)
