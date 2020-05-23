c = 0
cont= +1
nome = input('Nome do aluno:')
while (len(nome)<6 or len(nome)>100):
    nome=input('Digite seu nome novamente:')
dia = input('Digite o dia do seu nascimento:')
while (len(dia)<1 or len(dia)>31):
     dia=input('Digite o dia novamente:')
mês = input('Digite seu mês:')
while (len(mês) != [1,2,3,4,5,6,7,8,9,10,11,12]):
     mês=input('Digite o mês novamente:')
CPF = int(input('Insira seu CPF:'))
while (len(CPF)<11 or len(CPF)>11):
    CPF=input('Digite seu CPF novamente:')
responsavel = input('Nome do responsável:')
escola= input('Insira o nome da escola:')
turno = input('Insira o turno:')
while (len(turno)!=manhã or len(turno)!=tarde or len(turno)!=noite):
    turno=input('Digite seu turno novamente:')
