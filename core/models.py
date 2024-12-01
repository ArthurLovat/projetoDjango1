from django.db import models
from django.db.models import Model
from django.core.exceptions import ValidationError


class Paciente(models.Model): #def paciente de acordo com diagrama de classes
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    idade = models.PositiveIntegerField('Idade')
    cpf = models.CharField('CPF', max_length=11)
    email = models.EmailField('E-mail', max_length=100)
    telefone = models.CharField('Telefone', max_length=11)
    endereco = models.CharField("Endereço")
    nednereco = models.IntegerField('Numero', max_length=10)
    necessidade = models.TextField('Necessidade', max_length=3000)

    # função para encontar cuidador.Exemplo básico de busca de cuidadores com base na necessidade do paciente
    def encontarCuidador(self):
        return Cuidador.objects.filter(competencias_icontains=self.necessidade)

    # Atualiza informações do paciente com base nos parâmetros fornecidos
    def atualizarinformações(self, **kwargs):
        for attr, value in kwargs.items():
            setattr(self. attr, value)

        self.save()

    #validação de dados
    def clean(self):
        if not self.cpf.isdigit() or len(self.cpf) != 11:
            raise ValidationError('O CPF deve ter exatamente 11 digitos numericos.')
        #exemplo de validação de idade
        if self.idade < 0 or self.idade > 120:
            raise ValidationError('Idade Invalida!')

        super().clean()

    def __str__(self):
        return f'{self.nome} {self.sobrenome} {self.cpf} {self.idade}' #pode acrecentar mais informações na def caso necessario



class Cuidador(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    idade = models.PositiveIntegerField('Idade') #adicionar configuração para limitar maiores de 60 anos
    cpf = models.CharField('CPF', max_length=11)
    email = models.EmailField('E-mail', max_length=100)
    telefone = models.CharField('Telefone', max_length=11)
    competencias = models.TextField('Competencias', max_length=3000)

    def oferecerCuidado(self, paciente):
        # Exemplo de função para oferecer cuidado a um paciente
        # Pode incluir lógica para registrar que o cuidador está cuidando de um paciente
        # Este é um exemplo simples
        print(f'{self.nome} {self.sobrenome} está oferecendo cuidado ao paciente {paciente.nome} {paciente.sobrenome}')

    def atualizarDisponibilidade(self, disponibilidade):
        # Atualiza a disponibilidade do cuidador
        # Dependendo da implementação, você pode adicionar um campo para disponibilidade
        self.disponibilidade = disponibilidade
        self.save()

    # validação de dados
    def clean(self):
        if not self.cpf.isdigit() or len(self.cpf) != 11:
            raise ValidationError('O CPF deve ter exatamente 11 digitos numericos.')
        # exemplo de validação de idade
        if self.idade < 0 or self.idade > 120:
            raise ValidationError('Idade Invalida!')

        super().clean()

    def __str__(self):
        return f'{self.nome} {self.sobrenome} {self.idade} {self.cpf}'  # pode acrecentar mais informações na def caso necessario
