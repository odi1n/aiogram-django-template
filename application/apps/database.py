from config_db import *

TORTOISE_ORM = {
    'connections': {
        "default": f"postgres://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
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
