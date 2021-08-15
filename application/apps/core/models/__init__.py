from .user import User


def register_models() -> None:
    from tortoise import Tortoise

    Tortoise.init_models(models_paths=['apps.core.models'], app_label='core')
