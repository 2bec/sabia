from django.contrib import admin

from medicao.models import Medicao, IndicacaoClinica

# Register your models here.

admin.site.register(Medicao)
admin.site.register(IndicacaoClinica)