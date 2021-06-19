from django.contrib import admin
from .models import Animecharacter
# Register your models here.
@admin.register(Animecharacter)
class Animecharacteradmin(admin.ModelAdmin):
    list_display = ['id', 'alias_name', 'anime_name']