from django.contrib import admin
from .models import Paciente, Cuidador
from django.core.exceptions import ValidationError

class PacienteAdmin(admin.ModelAdmin):
     list_display = ('nome', 'sobrenome', 'idade', 'cpf')

     def save_model(self, request, obj, form, change):
         #validações personalizadas
        if not obj.cpf.isdigit() or len(obj.cpf) != 11:
            raise ValidationError('O CPF deve ter exatamente 11 digitos numericos!')
        super().save_model(request, obj, form, change,)

class CuidadorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'idade', 'cpf')

    def save_model(self, request, obj, form, change):
        # validações personalizadas
        if not obj.cpf.isdigit() or len(obj.cpf) != 11:
            raise ValidationError('O CPF deve ter exatamente 11 digitos numericos!')
        super().save_model(request, obj, form, change, )

admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Cuidador, CuidadorAdmin)
