from django.contrib import admin
from .models import Usuario

# Register your models here.
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome','email','senha','criadoem')
    search_fields = ('nome','email')
    readonly_fields = ('senha','criadoem')
    