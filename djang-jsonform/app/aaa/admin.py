from django.contrib.admin import register
from aaa.models import Aaa
from utils.admin import AbstractModelAdmin

@register(Aaa)
class AaaAdmin(AbstractModelAdmin):
    pass
