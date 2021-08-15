from aiogram import Dispatcher


def register_middlewares(dp: Dispatcher):
    from .example_middlewares import Example
    Example(dp)
