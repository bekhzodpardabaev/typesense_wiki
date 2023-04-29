from rest_framework import serializers
from vacancy.models import Vacancy, Category


class VacancySearchResultCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug')


class VacancySearchResultSerializer(serializers.ModelSerializer):
    category = VacancySearchResultCategorySerializer()

    class Meta:
        model = Vacancy
        fields = ('id', 'title', 'description', 'salary', 'category')
