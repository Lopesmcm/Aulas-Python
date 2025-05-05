codigo, quantidade  = list(map(int, input().split()))

if codigo == 1: 
    preco = 4
if codigo == 2: 
    preco = 4.5
if codigo == 3: 
    preco = 5
if codigo == 4: 
    preco = 2
if codigo == 5: 
    preco = 1.5

total = quantidade*preco
print(f'Total: R$ {total:.2f}')