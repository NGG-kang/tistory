from django.contrib.admin import register
from bbb.models import Bbb
from utils.admin import AbstractModelAdmin

@register(Bbb)
class BbbAdmin(AbstractModelAdmin):
    pass
