#Separados dígitos de um número
num = int(input('Digite um número: '))
'''n = str(num)
print('Analisando o número {}'.format(num))
print('Unidade: {}.'.format(n[3]))
print('Dezena: {}.'.format(n[2]))
print('Centena: {}.'.format(n[1]))
print('Milhar: {}.'.format(n[0]))
#Mas dá erro se rodar para um número com menos de 4 dígitos. 
#Outra forma de fazer:'''
# faz a divisão inteira por 1 e tira o módulo de 10. Mostra o resto da divisão
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}.'.format(u))
print('Dezena: {}.'.format(d))
print('Centena: {}.'.format(c))
print('Milhar: {}.'.format(m))