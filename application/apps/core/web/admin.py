from django.contrib import admin
from orm_converter import TortoiseToDjango

from .. import models


# Register your models here.
# To convert models: TortoiseToDjango.convert(models.ModelName)


@admin.register(TortoiseToDjango.convert(models.User))
class UserAdmin(admin.ModelAdmin):
    list_display = ['tg_id',
                    'chat_id',
                    'first_name']
