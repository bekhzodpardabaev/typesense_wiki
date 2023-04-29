import typesense


def get_typesense_client():
    return typesense.Client({
        'api_key': 'Hu52dwsas2AdxdE',
        'nodes': [{
            'host': 'localhost',
            'port': '8108',
            'protocol': 'http'
        }],
        'connection_timeout_seconds': 20
    })
