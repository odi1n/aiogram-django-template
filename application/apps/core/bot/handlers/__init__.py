from aiogram import Dispatcher


def register_handlers(dp: Dispatcher):
    from .test_handlers import Test

    Test(dp)
