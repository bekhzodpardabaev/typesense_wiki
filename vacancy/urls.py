from django.urls import path

from vacancy.views import (
    VacancySearchView,
    # VacancyDetailView,
    # RelatedVacanciesView,
)

urlpatterns = [
    path('search/', VacancySearchView.as_view(), name='vacancy_search'),
    # path('<int:pk>/', VacancyDetailView.as_view(), name='vacancy_detail'),
    # path('<int:pk>/related/', RelatedVacanciesView.as_view(), name='vacancy_related'),
]
