from aiogram import Dispatcher


def register_filter(dp: Dispatcher):
    from .example_filter import ExampleFilter
    ExampleFilter(dp)
