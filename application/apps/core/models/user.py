from tortoise import Tortoise, fields
from tortoise.models import Model


class User(Model):
    tg_id = fields.BigIntField(unique=True, description='Telegram User ID')
    chat_id = fields.BigIntField(unique=False, description='Telegram Chat ID')
    first_name = fields.CharField(max_length=64, description='Telegram Firstname')

    def __str__(self) -> str:
        return f'{self.first_name} - {self.tg_id}'

    class Meta:
        table = 'user'
