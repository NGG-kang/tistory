from django.contrib import admin
from django.utils.safestring import mark_safe

class AbstractModelAdmin(admin.ModelAdmin):
    list_display = ["queries_visualizing", "createdAt"]
    # list_display = ["queries", "createdAt"]

    def queries_visualizing(self, obj):
        return mark_safe("<br/>".join([f"{query["type"]} / {query["name"]}" for query in obj.queries]))
