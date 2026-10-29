import json, datetime as dt, os
def limpa():
    os.system("cls")
def menu():
    print(" ====== Menu de Transações Financeiras ====== ")
    print(formatdata)
def mostrar_ordenada(tipo_transacao,ordem):
    if tipo_transacao == "data":
        ordenada = sorted(transacoes, key=lambda t: dt.datetime.strptime(t['data'], "%d/%m/%Y"), reverse=ordem)
        limpa()
        print(f" ==== Transações ordenadas por {tipo_transacao} ==== ")
        for t in ordenada:
            limpa()
            print(f"ID da Transação : {t['id']}")
            print(f"Data da Transação : {t['data']}")
            print(f"Descrição : {t['descricao']}")
            print(f"Valor da Transação : {t['valor']:.2f}")
            print(f"Tipo da Transação : {t['tipo']}")
            tempo = input("Press any Key.\n")
            limpa()
    else:
        ordenada = sorted(transacoes, key=lambda t: t[tipo_transacao], reverse=ordem)
        limpa()
        print(f" ==== Transações ordenadas por {tipo_transacao} ==== ")
        for t in ordenada:
            limpa()
            print(f"ID da Transação : {t['id']}")
            print(f"Data da Transação : {t['data']}")
            print(f"Descrição : {t['descricao']}")
            print(f"Valor da Transação : {t['valor']:.2f}")
            print(f"Tipo da Transação : {t['tipo']}")
            tempo = input("Press any Key.\n")
            limpa()
def perguntar_ordem():
    print("<0> Ordenar Maior ao Menor\n<1> Ordenar Menor ao Maior")
    while True:
        try:
            ordem = int(input("Selecione uma opção : "))
            if ordem == 0:
                return True   
            elif ordem == 1:
                return False 
            else:
                print("Valor Inválido. Digite 0 ou 1.")
        except ValueError:
            print("Valor incorreto.")
    
    
now = dt.datetime.now()
formatdata = now.strftime("%d/%m/%Y - %H:%M:%S")


try:
    with open("transacoes.json", "r") as transacoes:
        transacoes = json.load(transacoes)
    print("'transacoes.json' Encontrado e Carregado")
    print()
    
        
except FileNotFoundError:
        print("'transacoes.json' não encontrado.")
        print()
        transacoes = []
        


case = 0
while case!=4:
    
    menu()
    print("<1> Adicionar\n<2> Listar\n<3> Ordenar\n<4> Sair e Salvar")
    while True:
        try:
            case = int(input("Escolha uma das opções\n"))
            break
        except ValueError:
            limpa()
            print("Valor Incorreto.")
            print("<1> Adicionar\n<2> Listar\n<3> Ordenar\n<4> Sair e Salvar")
            continue
        
        
            
    match case:
        case 1: # Caso  1 ==========================================================================================
            
            limpa()
            print("====== Menu Adicionar ======")
            idnew =  len(transacoes) + 1
            
            
            
            print("Deseja inserir descrição?\nCaso não, aperte Enter.\nCaso sim, preencha abaixo.")
            descricao = input("Descrição : ")
            if not descricao:
                descricao = "Sem descrição."
            limpa()
            print("====== Menu Adicionar ======")
            
            while True:
                data123 = input("Data da Transação (Dia/Mês/Ano): ") 
                try:
                    data1 = dt.datetime.strptime(data123, "%d/%m/%Y")
                    if data1 > dt.datetime.now():
                        print("A data não pode estar no futuro.")
                        continue
                    break
                except ValueError:
                    print("Valor inválido, a data dever ser formatada em Dia/Mês/Ano.")
                    continue
            limpa()
            while True:
                try:
                    
                    print("====== Menu Adicionar ======")
                    print()
                    print("== Valor ==")
                    valor = float(input("Digite o valor da transação (ex: 999.99): "))
                    break
                    
                except ValueError:
                    limpa()
                    print("Valor Inválido.")
                    
                    
            limpa()
            print("== Tipo de Transação ==")
            print("<1> Pix\n<2> Dinheiro\n<3> Crédito\n<4> Débito\n<5> Boleto")
            while True:
                tipo = -1
                while tipo>5 or tipo<1:
                    try:
                        tipo = int(input("Escolha um tipo de transação : "))
                        match tipo:
                            case 1: 
                                tipo1 = "pix"
                            case 2: 
                                tipo1 = "Dinheiro"
                            case 3: 
                                tipo1 = "Crédito"
                            case 4: 
                                tipo1 = "Débito"
                            case 5: 
                                tipo1 = "Boleto"
                            case _: 
                                print("Valor Inválido")
                        limpa()
                        print("Transação Criada.")
                        t = input("Press Any Key.")
                        limpa(
                            
                        )
                        break
            
                    except ValueError:
                        print("Valor Inválido.")
                    
                    

                novatransacao = {
                    "id" : idnew,
                    "data" : data1.strftime("%d/%m/%Y"),
                    "descricao" : descricao,
                    "valor" : float(valor),
                    "tipo" : tipo1
                }
                transacoes.append(novatransacao)
                break
        case 2:
            if len(transacoes)!=0:
                for i,t in enumerate(transacoes, start=1):
                    limpa()
                    print(f"====== Transação Nº{i} ======")
                    print(f"ID da Transação : {t['id']}")
                    print(f"Data da Transação : {t['data']}")
                    print(f"Descrição : {t['descricao']}")
                    print(f"Valor da Transação : {t['valor']:.2f}")
                    print(f"Tipo da Transação : {t['tipo']}")
                    tempo = input("Press any Key.\n")
                    limpa()
                    

            else:
                limpa()
                print("Sem transações cadastradas.")
        case 3:
            if len(transacoes) == 0:
                limpa()
                print("Sem transações cadastradas.")
            else:
                limpa()
                print("====== Menu Filtro ======")
                print("<1> Ordenar por Id\n<2> Ordenar por Valor\n<3> Ordenar por Data\n<4> Filtrar por Tipo\n<5> Sair")
                
                while True:
                    try:
                        caso = int(input("Escolha uma opção : "))
                        break
                    except ValueError: 
                        print("Valor incorreto")
                while caso !=5:
                    match caso:
                        case 1: 
                            tipo_transacao = "id"
                            limpa()
                            print("====== Menu Filtro ======")
                            ordem = perguntar_ordem()
                            mostrar_ordenada(tipo_transacao, ordem)
                            break
                        case 2:
                            tipo_transacao = "valor"
                            limpa()
                            print("====== Menu Filtro ======")
                            ordem = perguntar_ordem()
                            mostrar_ordenada(tipo_transacao, ordem)
                            break
                        case 3:
                            tipo_transacao = "data"
                            limpa()
                            print("====== Menu Filtro ======")
                            ordem = perguntar_ordem()
                            mostrar_ordenada(tipo_transacao, ordem)
                            break
                        case 4:
                            limpa()
                            
                            while True:
                                try:
                                    tipo2 = int(input("Escolha um tipo de transação\n<1> Pix\n<2> Dinheiro\n<3> Crédito\n<4> Débito\n<5> Boleto\n<0> Sair"))
                                    if tipo2>5 or tipo2<0:
                                        continue
                                    else:
                                        break
                                    
                                except ValueError:
                                    print("Valor Inválido.")
                            if tipo2 ==0:
                                limpa()
                                break
                            else:
                                tipos = {1 : "Pix", 2 : "Dinheiro", 3 : "Crédito", 4:"Débito", 5: "Boleto"}
                                tipoescolhido = tipos[tipo2]
                                filtradas = []
                                for t in transacoes:
                                    if t['tipo'].lower() == tipoescolhido.lower():
                                        filtradas.append(t)
                                if len(filtradas) == 0:
                                    limpa()
                                    print(f"Nenhuma transação do tipo '{tipos[tipo2]}'encontrada.")
                                    tempo = input("Press any Key.\n")
                                else:
                                    limpa()
                                    for i in filtradas:
                                        limpa()
                                        print(f"ID da Transação : {i['id']}")
                                        print(f"Data da Transação : {i['data']}")
                                        print(f"Descrição : {i['descricao']}")
                                        print(f"Valor da Transação : {i['valor']:.2f}")
                                        print(f"Tipo da Transação : {i['tipo']}")

                                        tempo = input("Press any Key.\n")
                                        limpa()
                                
                        case _:
                            print("Valor Inválido.")
                limpa()
        case 4:
            if len(transacoes) !=0:
                limpa()
                
                while True:
                    
                    print("Deseja salvar as alterções feitas?")
                    try:
                        salvar = int(input("<1> Sim\n<2> Não\n\n<0> Apagar .json salvo\n"))
                        match salvar:
                            case 0:
                                arquivo = "transacoes.json"
                                os.remove(arquivo)
                                limpa()
                                print("Arquivo 'transacoes.json' deletado.")
                            case 1:
                                limpa()
                                with open("transacoes.json","w") as arquivo:
                                    json.dump(transacoes, arquivo, ensure_ascii=False)
                                print("'transacoes.json' salvo.")
                                print("Você saiu.")
                            case 2:
                                limpa()
                                print("Você saiu.")
                            case _:
                                print("Caso Inválido.")
                        break
                    except ValueError:
                        limpa()
                        print("Valor Inválido")
            else:
                limpa()
                print("Sem modificações para salvar.")
                print("Você saiu.")
        case _:
            limpa()
            print("Valor Inválido, Tente Novamente.")

                                        
        
        # CASO 3 - caso 4
        # CASO 4