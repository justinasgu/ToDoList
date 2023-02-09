from django.db import models
from django.contrib.auth.models import User


class Uzduotis(models.Model):
    uzduoties_tekstas = models.CharField(verbose_name='Užduoties tekstas', help_text='Įveskite užduotį (pvz. padaryti baigiamąjį projektą)', max_length=300, null=True)
    vartotojas = models.ForeignKey(to=User, verbose_name='User', on_delete=models.SET_NULL, null=True, blank=True)
    data = models.DateField(verbose_name='Data', null=True)

    def __str__(self):
        return f"Prisijungęs vartotojas ({self.vartotojas}) ir jo užduotis: „{self.uzduoties_tekstas}“"

    class Meta:
        verbose_name = "Užduotis"
        verbose_name_plural = "Užduotys"
        ordering = ['-data']