from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Actresses
from django.db.models import QuerySet

@admin.register(Actresses)
class ActressesAdmin(admin.ModelAdmin):
    list_display = ['number','name', 'surname', 'name_rus', 'surname_rus', 'age', 'date_of_birth', 'sign_zodiac',
                    'city_of_birth', 'biography','image']
    list_editable = ['name','surname', 'name_rus', 'surname_rus', 'age', 'date_of_birth', 'sign_zodiac',
                     'city_of_birth', 'biography','image']

