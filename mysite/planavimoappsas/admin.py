from django.contrib import admin
from .models import Uzduotis


class UzduotisAdmin(admin.ModelAdmin):
    list_display = ('uzduoties_tekstas', 'vartotojas', 'data')
    list_filter = ('vartotojas', 'data')


admin.site.register(Uzduotis, UzduotisAdmin)
