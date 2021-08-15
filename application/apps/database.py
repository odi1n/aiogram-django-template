from os import getenv

TORTOISE_ORM = {
    'connections': {
        'host': getenv('DB_HOST'),
        'port': getenv('DB_PORT'),
        'user': getenv('DB_USER'),
        'password': getenv('DB_PASSWORD'),
        'database': getenv('DB_NAME'),
    },
    'apps': {
        "models": {
            "models": [
                "aerich.models",
                "apps.core.models",
            ],
            "default_connection": "default",
        },
    },
}
