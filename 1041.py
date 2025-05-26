coordenadax, coordenaday  = list(map(float, input().split()))

if coordenadax == 0 and coordenaday == 0: 
   print("Origem")
else:
    if coordenadax == 0:
        print ("Eixo y") 
    elif coordenaday == 0:
        print ("Eixo x")     
    elif coordenaday > 0:
        if coordenadax > 0:
            print("Q1") 
        else:
            print("Q2") 
    else:
        if coordenadax > 0:
            print ("Q4")     
        else: 
            print("Q3")
    
    


if coordenaday>0:
    if coordenadax>0:
        print("Q1")
    elif coordenadax <0 :
        print("Q2")
    else:
        print("Eixo y")
elif coordenaday < 0:
    if coordenadax>0:
        print("Q4")
    elif coordenadax <0 :
        print("Q3")
    else:
        print("Eixo y")
else:
    if coordenadax ==0:
        print("Origem")
    else:
        print("Eixo X")
