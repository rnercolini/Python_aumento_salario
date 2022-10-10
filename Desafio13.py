# Calcula o aumento percentual no salário de um funcionário
s = float(input('Digite o valor do salário do funcionário: R$'))
ns = s + (s * 15/100)
print('O valor do salário com o aumento de 15% é de R${:.2f}'.format(ns))
