from aiogram import Dispatcher
from aiogram.dispatcher.filters import BoundFilter, Filter


def register_filter(dp: Dispatcher):
    from .example_filter import Example
    Example(dp)
