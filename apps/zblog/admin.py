from django.contrib import admin

from .models import *
from .form import EntryModelForm


class EntryModelAdmin(admin.ModelAdmin):
    form = EntryModelForm


admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Entry, EntryModelAdmin)
