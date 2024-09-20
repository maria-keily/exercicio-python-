num1 = float(input('Primeira nota do aluno: '))
num2 = float(input('Segunda nota do aluno:  '))
num3 = float(input('Terceira nota do aluno: '))

media = (num1 + num2 + num3) / 2
print('A média entre {:.1f} e {:.1f} é igual a {:.1f}'.format (num1, num2, num3, media))
