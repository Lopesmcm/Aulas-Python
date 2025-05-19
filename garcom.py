bandeja = int(input ())

i = 0
qtd_quebrados = 0
while i<bandeja:
    
    i+=1
    lata, copo  = list(map(int, input().split()))
    if lata > copo : 
        qtd_quebrados += copo

print(qtd_quebrados)