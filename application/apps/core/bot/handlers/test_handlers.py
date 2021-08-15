from aiogram import Dispatcher
from aiogram.types import Message

import logger
from apps.core import services
from config.apps import INSTALLED_APPS

class Test:
    def __init__(self, dp: Dispatcher):
        @dp.message_handler(commands=['test'])
        async def test(message: Message):
            logger.log.info("dasd")
            await message.answer(message.text)

        @dp.message_handler(commands=["start"])
        async def start(message: Message):
            user, is_created = await services.add_user(
                tg_id=message.from_user.id,
                chat_id=message.chat.id,
                first_name=message.from_user.first_name)

            if is_created:
                await message.answer('You have successfully registered in the bot!')
            else:
                await message.answer('You are already registered in the bot!')

        @dp.message_handler(commands=["id"])
        async def send_my_id(message: Message):
            await message.answer(f'User Id: <b>{message.from_user.id}</b>\n'
                                 f'Chat Id: <b>{message.chat.id}</b>')

        @dp.message_handler(commands=["apps"])
        async def send_my_apps(message: Message):
            apps_names = ''
            for app in INSTALLED_APPS:
                apps_names += app.Config.name + '\n'

            await message.answer('Installed apps:\n'
                                 f'{apps_names}')

        @dp.message_handler(commands=["core"])
        async def simple_handler(message: Message):
            await message.answer('Hello from "Core" app!')
