#AGENDAMENTO
import datetime

c = 0
cont= +1
nome = input('Nome do aluno:')
while (len(nome)<6 or len(nome)>30):
    nome=input('Digite seu nome novamente:')
data = input('Data de nascimento:')

while (len(nome)<6 or len(nome)>30):
    nome=input('Digite seu nome novamente:')
CPF = int(input('Insira seu CPF:'))
responsavel = input('Nome do responsável:')
escola= input('Insira o nome da escola:')
turno = input('Insira o turno:')
