nome = input()
salario_fixo = float(input())
salario_variavel = 0.15*(float(input()))

total = salario_fixo + salario_variavel

print(f"TOTAL = R$ {total:.2f}")