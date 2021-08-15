from aiogram import Dispatcher


def register_bot(dp: Dispatcher):
    from .filters import register_filter
    from .handlers import register_handlers
    from .middlewares import register_middlewares

    register_middlewares(dp)
    register_handlers(dp)
    register_middlewares(dp)
