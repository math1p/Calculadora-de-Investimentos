print("Calculadora de investimentos <3")

def info_invest():
    valor = float(input("Valor inicial: "))
    taxa = float(input("Taxa (em % por ano): "))
    tempo = float(input("Tempo (em meses): "))
    return valor, taxa, tempo

def calc_invest(valor, taxa, tempo):                            #Calcular o montante
    return round(valor * (1 + taxa / 100 / 12) ** tempo, 2)

def calc_invest_ir(valor, taxa, tempo):                         #Calcular o montante com IR
    montante = calc_invest(valor, taxa, tempo)
    rendimento = montante - valor
    if tempo <= 6: #180
        return round(rendimento * (1 - 0.225) + valor, 2)
    elif 7 <= tempo <= 12: #360
        return round(rendimento * (1 - 0.20) + valor, 2)
    elif 13 <= tempo <= 24: #720
        return round(rendimento * (1 - 0.175) + valor, 2)
    else:
        return round(rendimento * (1 - 0.15) + valor, 2)

mode = int(input("Selecione o modo: (somente número)\n1 - Montante\n2 - Montante (IR regressivo (CDB))\n"))

if mode == 1:
    valor, taxa, tempo = info_invest()
    result_sem_ir = calc_invest(valor, taxa, tempo)
    rendimento_sem_ir = round(result_sem_ir - valor, 2)
    print("O montante será de R${:.2f}".format(result_sem_ir), "ao longo de", round(tempo), "meses. Rendendo R${:.2f}".format(rendimento_sem_ir))
    
elif mode == 2:
    valor, taxa, tempo = info_invest()
    result_com_ir = calc_invest_ir(valor, taxa, tempo)
    result_sem_ir = calc_invest(valor, taxa, tempo)
    rendimento_ir = round(result_com_ir - valor, 2)
    ir = round(result_sem_ir - result_com_ir, 2) 
    print("O montante com Imposto de Renda será de R${:.2f}".format(result_com_ir), "com rendimento de R${:.2f}".format(rendimento_ir), "ao longo de", round(tempo), "meses. R${:.2f}".format(ir), "foram destinados ao IR")
    
else:
    print("Modo inválido.")
