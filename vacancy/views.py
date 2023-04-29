from rest_framework.generics import ListAPIView
from vacancy.serializers import VacancySearchResultSerializer
from vacancy.filter_backends import TypesenseSearchFilterBackend
from vacancy.models import Vacancy


# Create your views here.

class VacancySearchView(ListAPIView):
    serializer_class = VacancySearchResultSerializer
    filter_backends = [TypesenseSearchFilterBackend]
    typesense_search_schema = {
        'query_by': 'category.name_uz,category.name_ru,category.name_en,title',
        'sort_by': 'published_at:asc',
    }
    queryset = Vacancy.objects.filter(
        is_visible=True
    )

#
# class VacancyDetailView: ...
#
#
# class RelatedVacanciesView: ...
