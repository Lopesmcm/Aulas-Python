duracao_segundos = int(input()) 

conversao_horas = (duracao_segundos//3600)

resto = (duracao_segundos % 3600)

conversao_minutos = (resto // 60) 

conversao_segundos = (resto%60) 


print(f"{conversao_horas}:{conversao_minutos}:{conversao_segundos}")