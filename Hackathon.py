c = 0
cont= +1
nome = input('Nome do aluno:')
while (len(nome)<6 or len(nome)>30):
    nome=input('Digite seu nome novamente:')
data = input('Data de nascimento(Coloque as barras):')
CPF = int(input('Insira seu CPF:'))
while (len(CPF)<11 or len(CPF)>11):
    nome=input('Digite seu CPF novamente:')
responsavel = input('Nome do responsável:')
escola= input('Insira o nome da escola:')
turno = input('Insira o turno:')
while (len(turno)!=manhã or len(turno)!=tarde or len(turno)!=noite):
    nome=input('Digite seu turno novamente:')
