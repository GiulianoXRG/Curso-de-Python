n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
soma = n1 + n2 
sub = n1 - n2
multi = n1 * n2
div = n1 / n2
di = n1 // n2
expo = n1 ** n2
rest = n1 % n2
print(f'A soma é {soma} ,\n a subtração é {sub} \n, o produto é {multi} e a divisão é {div :.2f} ', end='')
# end='' para não quebrar a linhas,  \n para quebrar a linha 
print(f'A divisão inteira é {di}, a exponenciação é {expo} e o resto da divisão é {rest}')