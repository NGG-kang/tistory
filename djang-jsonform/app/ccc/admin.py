from django.contrib.admin import register
from ccc.models import Ccc
from utils.admin import AbstractModelAdmin

@register(Ccc)
class CccAdmin(AbstractModelAdmin):
    pass
