from django.db import models


class Denuncia(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('concluida', 'Concluída'),
        ('resolvido', 'Resolvido'),  # Caso deseje outro status
    ]

    nome = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default='pendente')

    def __str__(self):
        if self.nome:
            return f"{self.nome} - {self.data_criacao}"
        return f"Anônimo - {self.data_criacao}"

    # Métodos adicionais para a visualização de campos no Admin
    def get_nome(self):
        return self.nome if self.nome else "Anônimo"
    get_nome.short_description = 'Nome'

    def get_email(self):
        return self.email if self.email else "Não informado"
    get_email.short_description = 'Email'
