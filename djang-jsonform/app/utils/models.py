from django.db import models
from django_jsonform.models.fields import JSONField


class AbstractModel(models.Model):
    QUERIES_SCHEMA = {
        "type": "list",
        "items": {
            "type": "dict",
            "keys": {
                "type": {"type": "string", "choices": ["choice1", "choice2"]},
                "name": {"type": "string"},
            },
        },
    }
    queries = JSONField(schema=QUERIES_SCHEMA)
    createdAt = models.DateTimeField(null=True, auto_now_add=True)

    class Meta:
        abstract = True
