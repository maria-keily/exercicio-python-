#1: ** Potência, 2: * Mult, 3:/ Divisão, 4: // Divisão inteira, 5: % resto da divisão

n1 = int(input('Digite um valor: '))
n2 = int(input('Outro valor: '))
soma = n1 + n2 
mult = n1 * n2
div = n1 / n2
divInt = n1 // n2
poten = n1 ** n2
print('A soma é {}, o produto e a divisão é {:.3f}' .format(soma, mult, div, divInt, poten), end= '')
print('Divisão Inteira {} e potência {}' .format(div, poten))
