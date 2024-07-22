#Ângela, uma nutricionista, precisa fazer a triagem de um grupo de 10 pacientes. Para cada paciente ela precisa saber qual o IMC do paciente de acordo com o peso e a altura informado. 
# Crie um programa que ajude a Ângela a fazer esta atividade com facilidade.


# Parte II
# Modifique o programa para receber um numero indefinido de pacientes.

########## PARTE 1

# qtdPacientes = 10

# for i in range(qtdPacientes):
#     i += 1
#     print(f'Paciente numero {i}')
#     paciente = input('Insira o nome do paciente: ')
#     peso = int(input('Insira o peso: '))
#     altura = float(input('Insira a altura: '))
#     total = (f'{peso / (altura**2):.2f}')
    
    
#     print(f'Peso de {paciente} é {peso} e sua altura é {altura} e seu IMC é de {total}')

########## PARTE 2

i = 0

while True:
    i += 1
    print(f'Paciente numero {i}')
    paciente = input('Insira o nome do paciente: ')
    peso = int(input('Insira o peso: '))
    altura = float(input('Insira a altura: '))
    total = (f'{peso / (altura**2):.2f}')
    
    print(f'Peso de {paciente} é {peso} e sua altura é {altura} e seu IMC é de {total}')
    continuar = input(f'Deseja continuar? (S/N) ').lower()
    if(continuar != 's'):
        print(f'Tudo bem, até mais!')
        break
    
