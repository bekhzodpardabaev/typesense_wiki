from config import get_typesense_client
from typesense.collection import Collection
from typesense import Client


def _empty_str_if_none(value):
    return value if value else ''


class VacancyTypeSense:
    COLLECTION_NAME = "vacancy"
    client: Client = get_typesense_client()
    collection: Collection = client.collections[COLLECTION_NAME]

    @classmethod
    def create_collection(cls):
        vacancy_collection_scheme = {
            'name': cls.COLLECTION_NAME,
            'fields': [
                {"name": "id", "type": "int32"},
                {"name": "title", "type": "string"},
                {"name": "published_at", "type": "int32"},
                {"name": "category.id", "type": "int32", "facet": True},
                {"name": "category.name_uz", "type": "string", "locale": "uz"},
                {"name": "category.name_ru", "type": "string", "locale": "ru"},
                {"name": "category.name_en", "type": "string", "locale": "en"},
                {"name": "category.slug", "type": "string"}
            ],
            "default_sorting_field": "published_at"
        }
        return cls.client.collections.create(vacancy_collection_scheme)

    @classmethod
    def create_vacancy(cls, vacancy):
        return cls.collection.documents.create({
            "id": str(vacancy.id),
            "title": vacancy.title,
            "published_at": int(vacancy.published_at.timestamp()),
            "category.id": vacancy.category.id,
            "category.name_uz": _empty_str_if_none(vacancy.category.name_uz),
            "category.name_ru": _empty_str_if_none(vacancy.category.name_ru),
            "category.name_en": _empty_str_if_none(vacancy.category.name_en),
            "category.slug": vacancy.category.slug
        })

    @classmethod
    def update_vacancy(cls, vacancy):
        return cls.collection.documents.update({
            "id": str(vacancy.id),
            "title": vacancy.title,
            "published_at": int(vacancy.published_at.timestamp()),
            "category.id": vacancy.category.id,
            "category.name_uz": _empty_str_if_none(vacancy.category.name_uz),
            "category.name_ru": _empty_str_if_none(vacancy.category.name_ru),
            "category.name_en": _empty_str_if_none(vacancy.category.name_en),
            "category.slug": vacancy.category.slug
        })

    @classmethod
    def delete_vacancy(cls, vacancy):
        return cls.collection.documents[vacancy.id].delete()
