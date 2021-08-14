from typing import Optional

from aiogram import Dispatcher
from django.apps import AppConfig


def register(dp: Optional[Dispatcher] = None) -> None:
    """
    The function registers the app.

    :param dp:
        If Dispatcher is not None — register bots modules.
    """
    from .models import register_models
    register_models()

    if dp is not None:
        from .bot.handlers import register_handlers, RegisterHandlers
        from .bot.middlewares import register_middlewares
        from .bot.filters import register_filters

        register_middlewares(dp)
        register_filters(dp)
        register_handlers(dp)
        RegisterHandlers(dp)


class Core(AppConfig):
    """Django App Config"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.core'
    verbose_name = 'core'

    @staticmethod
    def convert_models():
        from orm_converter import TortoiseToDjango
        from . import models

        TortoiseToDjango.convert_from_module(module=models)

    def ready(self):
        from .web import admin  # type: ignore

        self.convert_models()
