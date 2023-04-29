import typesense
import json
from faker import Faker

client = typesense.Client({
    'api_key': 'Hu52dwsas2AdxdE',
    'nodes': [{
        'host': 'localhost',
        'port': '8108',
        'protocol': 'http'
    }],
    'connection_timeout_seconds': 20
})


def create_api_key():
    key = client.keys.create({
        "description": "Admin key.",
        "actions": ["*"],
        "collections": ["*"]
    })
    print(key)


def create_collection():
    create_response = client.collections.create({
        'name': 'merchants',
        'fields': [
            {"name": "id", "type": "string"},
            {"name": "title_uz", "type": "string", "locale": "uz"},
            {"name": "title_ru", "type": "string", "locale": "ru"},
            {"name": "title_en", "type": "string", "locale": "en"},
            {"name": "typo_searches_uz", "type": "string[]", "locale": "uz"},
            {"name": "typo_searches_ru", "type": "string[]", "locale": "ru"},
            {"name": "typo_searches_en", "type": "string[]", "locale": "en"},
            {"name": "content_uz", "type": "string", "locale": "uz"},
            {"name": "content_ru", "type": "string", "locale": "ru"},
            {"name": "content_en", "type": "string", "locale": "en"},
            {"name": "category", "type": "string", "facet": True},
            {"name": "published_at", "type": "int32"},
            {"name": "views_count", "type": "int32"},
            {"name": "likes_count", "type": "int32"},
            {"name": "comments_count", "type": "int32"},
            {"name": "weight", "type": "int32"}
        ],
    })

    return create_response


def add_documents():
    # create fake news
    faker = Faker()
    # for i in range(100000):
    #     print(i)
    #     client.collections['news'].documents.create({
    #         'title_uz': faker.sentence(),
    #         'title_ru': faker.sentence(),
    #         'title_en': faker.sentence(),
    #         'content_uz': faker.text(),
    #         'content_ru': faker.text(),
    #         'content_en': faker.text(),
    #         'category': faker.word(),
    #         'published_at': int(faker.date_time().timestamp()),
    #         'views_count': faker.random_int(),
    #         'likes_count': faker.random_int(),
    #         'comments_count': faker.random_int(),
    #         'weight': faker.random_int()
    #     })

    client.collections['merchants'].documents.create({
        'title_uz': 'Beeline',
        'title_ru': 'Beeline',
        'title_en': 'Beeline',
        'typo_searches_uz': ['bilayn', 'belayn'],
        'typo_searches_ru': [],
        'typo_searches_en': [],
        'content_uz': faker.text(),
        'content_ru': faker.text(),
        'content_en': faker.text(),
        'category': faker.word(),
        'published_at': int(faker.date_time().timestamp()),
        'views_count': faker.random_int(),
        'likes_count': faker.random_int(),
        'comments_count': faker.random_int(),
        'weight': faker.random_int()
    })


def change_documents():
    client.collections['merchants'].documents.update(
        {
            'id': '4094',
            'tags': ['tag1', 'tag3']

        }
    )
    override = {
        "rule": {
            "query": "category:laugh",
            "match": "exact"
        },
        "includes": [
            {"id": "50643", "position": 1},
        ],
        "excludes": [
            {"id": "61192"}
        ]
    }
    client.collections['merchants'].overrides.upsert('customize-tags', override)


def search():
    search_parameters = {
        'q': 'lorem',
        'query_by': 'title_uz,title_ru,title_en,content_uz,content_ru,content_en',
        'sort_by': 'weight:desc',
    }

    return client.collections['merchants'].documents.search(search_parameters)


if __name__ == "__main__":
    # create_api_key()
    create_collection()
    add_documents()
    # print(search())
    # change_documents()
    with open("response.json", "w") as f:
        json.dump(
            client.collections['merchants'].documents.search({
                'q': 'bilayn',
                'query_by': 'title_uz,title_ru,title_en,typo_searches_uz',
                'per_page': 30,
            }),
            f, indent=4
        )
