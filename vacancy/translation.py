from modeltranslation.translator import register, TranslationOptions

from vacancy.models import Category


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)
