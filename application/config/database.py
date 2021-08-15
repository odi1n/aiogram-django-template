from os import getenv
from typing import Dict, Type, Set

from config_db import *

from tortoise import Model


class DatabaseConfig:
    @staticmethod
    def get_tortoise_config():
        return {
            'connections': {
                'default': {
                    'engine': 'tortoise.backends.asyncpg',
                    'credentials': {
                        'host': DB_HOST,
                        'port': DB_PORT,
                        'user': DB_USER,
                        'password': DB_PASSWORD,
                        'database': DB_NAME,
                    }
                },
            },
            'apps': _get_inited_tortoise_apps(),
            'use_tz': False,
            'timezone': 'UTC'
        }

    @staticmethod
    def get_django_config():
        return {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'HOST': DB_HOST,
                'PORT': DB_PORT,
                'USER': DB_USER,
                'PASSWORD': DB_PASSWORD,
                'NAME': DB_NAME,
            }
        }


def _get_inited_tortoise_apps() -> Dict[str, Dict[str, Set[str]]]:
    """
    Retrieves all registered apps for Tortoise Config

    :return: Dict of Apps for Tortoise Config
    """
    from tortoise import Tortoise

    apps = {}
    for app_name, app_models in Tortoise.apps.items():  # type: str, Dict[str, Type[Model]]
        for model_name, model_type in app_models.items():
            try:
                apps[app_name]['models'] |= {model_type.__module__}
            except KeyError:
                apps[app_name] = {'models': {model_type.__module__}}
    return apps
