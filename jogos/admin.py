from django.contrib import admin

# Register your models here.

from django.contrib import admin
from jogos.models import Jogos


class Games(admin.ModelAdmin):
    list_display = ('id', 'nome','preco', 'data_lancamento')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', 'preco', 'data_lancamento')
    list_per_page = 20


admin.site.register(Jogos, Games)
