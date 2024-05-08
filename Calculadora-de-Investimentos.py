while True:
    print("Calculadora de Rendimentos <3 \nPor Matheus Pestana \n")

    def info_invest():                                              #Dados básicos
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

    mode = int(input("Selecione o modo: (somente número)\n1 - Montante\n2 - Montante (IR regressivo (CDB))\n3 - Comparar 2 investimentos\n"))

    result_invest1 = 0  # Definindo com valor padrão
    result_invest2 = 0  # Definindo com valor padrão
    comp_result = 0
    comp_rend = 0


    if mode == 1:
        valor, taxa, tempo = info_invest()
        result_sem_ir = calc_invest(valor, taxa, tempo)
        rendimento_sem_ir = round(result_sem_ir - valor, 2)
        print()
        print("O montante será de R${:.2f}".format(result_sem_ir), "ao longo de", round(tempo), "meses. Rendendo R${:.2f}".format(rendimento_sem_ir))
        print()
    
    elif mode == 2:
        valor, taxa, tempo = info_invest()
        result_com_ir = calc_invest_ir(valor, taxa, tempo)
        result_sem_ir = calc_invest(valor, taxa, tempo)
        rendimento_ir = round(result_com_ir - valor, 2)
        ir = round(result_sem_ir - result_com_ir, 2) 
        print()
        print("O montante com Imposto de Renda será de R${:.2f}".format(result_com_ir), "com rendimento de R${:.2f}".format(rendimento_ir), "ao longo de", round(tempo), "meses. O valor do IR será R${:.2f}".format(ir))
        print()

    elif mode == 3:
        ir_or_no = input("É cobrado IR no investimento 1? (S/N)\n").lower() #add suporta para vírgula
        if ir_or_no =='s':
            print()
            valor, taxa, tempo = info_invest()
            result_invest1 = calc_invest_ir(valor, taxa, tempo) #chamar de invest1
            #result_sem_ir = calc_invest(valor, taxa, tempo)
            rend_invest1 = round(result_invest1 - valor, 2)
            #ir = round(result_sem_ir - result_com_ir, 2)
            tempo_invest1 = tempo
            print()

        elif ir_or_no == 'n':
            print()
            valor, taxa, tempo = info_invest()
            result_invest1 = calc_invest(valor, taxa, tempo)
            rend_invest1 = round(result_invest1 - valor, 2)
            tempo_invest1 = tempo
            print()

        else:
            print()
            print("Resposta inválida, digite 's' ou 'n'")
            print()

        ir_or_no = input("É cobrado IR no investimento 2? (S/N)\n").lower()
        if ir_or_no == 's':
            print()
            valor, taxa, tempo = info_invest()
            result_invest2 = calc_invest_ir(valor, taxa, tempo) #chamar de invest2
            #result_sem_ir = calc_invest(valor, taxa, tempo)
            rend_invest2 = round(result_invest2 - valor, 2)
            #ir = round(result_sem_ir - result_com_ir, 2)
            tempo_invest2 = tempo
            print()

        elif ir_or_no == 'n':
            print()
            valor, taxa, tempo = info_invest()
            result_invest2 = calc_invest(valor, taxa, tempo)
            rend_invest2 = round(result_invest2 - valor, 2)
            tempo_invest2 = tempo
            print()       
         
        else:
            print()
            print("Resposta inválida, digite 's' ou 'n'")
            print()

        if rend_invest1 >= rend_invest2:
            maior_rend = rend_invest1
            menor_rend = rend_invest2
        else:
            maior_rend = rend_invest2
            menor_rend = rend_invest1

        if result_invest1 >= result_invest2:
            comp_result = result_invest1 - result_invest2
            comp_rend = maior_rend - menor_rend
            maior_result = result_invest1
            menor_result = result_invest2
            maior_result_str = "investimento 1"
            menor_result_str = "investimento 2"
            tempo_maior_result = tempo_invest1
            tempo_menor_result = tempo_invest2


        elif result_invest2 >= result_invest1:
            comp_result = result_invest2 - result_invest1
            comp_rend = maior_rend - menor_rend
            maior_result = result_invest2
            menor_result = result_invest1
            maior_result_str = "investimento 2"
            menor_result_str = "investimento 1"
            tempo_maior_result = tempo_invest2
            tempo_menor_result = tempo_invest1

        print(maior_result_str.capitalize(),": O montante será de R${:.2f}".format(maior_result))
        print(menor_result_str.capitalize(),": O montante será de R${:.2f}".format(menor_result))
        print()

        if comp_result == comp_rend:    #não testado
            print("O montante do", maior_result_str, "será R${:.2f}".format(comp_result),"maior que o montante do", menor_result_str)          

        else:
            print("O montante do", maior_result_str, "será R${:.2f}".format(comp_result),"maior que o montante do", menor_result_str)
            print("O rendimento do", maior_result_str, "será R${:.2f}".format(comp_rend),"maior que o montante do", menor_result_str)

    else:
        print()
        print("Modo inválido.")
        print()

    print()
    print("Pressione Enter para reiniciar ou digite 's' para sair...")
    resposta = input().lower()
    if resposta == 's':
        break  # Sai do loop se o usuário digitar 's'