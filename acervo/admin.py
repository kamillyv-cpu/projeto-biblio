from django.contrib import admin
from .models import Livro, Autor

class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_lancamento', 'resumo', 'nome_editora')
    search_fields = ('titulo',)

admin.site.register(Livro, LivroAdmin)

class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'ano_nascimento')
    search_fields = ('nome',)

admin.site.register(Autor,AutorAdmin)
