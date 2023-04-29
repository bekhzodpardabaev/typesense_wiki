from django.contrib import admin
from vacancy import models


@admin.register(models.Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_filter = ('category', 'is_visible')
    list_display = ('title', 'category', 'salary', 'is_visible')
    search_fields = ('title', 'description', 'id')


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug', 'id')


@admin.register(models.CategorySynonyms)
class CategorySynonymsAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'root_word', 'words')
