from aiogram import Dispatcher


def register_handlers(dp: Dispatcher):
    from .example_handlers import ExampleHandlers

    ExampleHandlers(dp)
