from django.db.models.signals import post_save, post_delete
from vacancy.models import Vacancy, Category, CategorySynonyms
from vacancy.typesense_helpers import VacancyTypeSense
import typesense.exceptions


def vacancy_post_save_handler(sender, instance, created, *args, **kwargs):
    if created:
        VacancyTypeSense.create_vacancy(instance)
    else:
        VacancyTypeSense.update_vacancy(instance)


def vacancy_post_delete_handler(sender, instance, *args, **kwargs):
    try:
        VacancyTypeSense.delete_vacancy(instance)
    except typesense.exceptions.ObjectNotFound:
        pass


def category_post_save_handler(sender, instance, created, *args, **kwargs):
    if not created:
        for vacancy in instance.vacancy_set.iterator():
            VacancyTypeSense.update_vacancy(vacancy)


def category_synonyms_post_save_handler(sender, instance: CategorySynonyms, created, *args, **kwargs):
    if created and instance.is_active or not created and instance.is_active:
        print("create or update")
        VacancyTypeSense.collection.synonyms.upsert(
            instance.id,
            instance.construct_typesense_synonyms()
        )
    else:
        print("delete")
        try:
            VacancyTypeSense.collection.synonyms[instance.id].delete()
        except typesense.exceptions.ObjectNotFound:
            pass


def category_synonyms_post_delete_handler(sender, instance: CategorySynonyms, *args, **kwargs):
    try:
        VacancyTypeSense.collection.synonyms[instance.id].delete()
    except typesense.exceptions.ObjectNotFound:
        pass


def connect_signal_handlers():
    post_save.connect(vacancy_post_save_handler, sender=Vacancy)
    post_delete.connect(vacancy_post_delete_handler, sender=Vacancy)
    post_save.connect(category_post_save_handler, sender=Category)

    post_save.connect(category_synonyms_post_save_handler, sender=CategorySynonyms)
    post_delete.connect(category_synonyms_post_delete_handler, sender=CategorySynonyms)
