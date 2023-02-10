from django.contrib import admin
from .models import Uzduotis


class UzduotisAdmin(admin.ModelAdmin):
    list_display = ('uzduotis', 'vartotojas', 'sukurta')
    list_filter = ('vartotojas', 'sukurta')


admin.site.register(Uzduotis, UzduotisAdmin)
