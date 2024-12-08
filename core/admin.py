from django.contrib import admin
from .models import Denuncia


@admin.register(Denuncia)
class DenunciaAdmin(admin.ModelAdmin):
    list_display = ('get_nome', 'get_email', 'status', 'data_criacao')
    list_filter = ('status', 'data_criacao')
    search_fields = ('nome', 'email', 'descricao')

    # Campos somente de leitura, o conteúdo não pode ser modificado
    readonly_fields = ('get_nome', 'get_email', 'descricao')

    # Campos editáveis
    fields = ('get_nome', 'get_email', 'descricao', 'status')

    # Ações
    def get_nome(self, obj):
        return obj.nome if obj.nome else "Anônimo"
    get_nome.short_description = 'Nome'

    def get_email(self, obj):
        return obj.email if obj.email else "Não informado"
    get_email.short_description = 'Email'
