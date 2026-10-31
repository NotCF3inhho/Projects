import os,json,random, time
def limpa():
    os.system("cls")
try:
    with open("perguntas.json", "r") as gb:
        perguntasx = json.load(gb)
    print("Perguntas carregadas.")
    print()
except FileNotFoundError:
    perguntas = []
    print("Arquivos não encontrados")
    print()
    while True:
        try:
            print("====== Defina perguntas ======")
            qntd = int(input("Qntd de Perguntas: "))
            break
        except ValueError:
            limpa()
            print("Valor inválido")
            continue
    for i in range(qntd):
        print(f"Questão {i+1} - ")
        pergunta = input("Pergunta : ")
        a = input("Alternativa A: ")
        b = input("Alternativa B: ")
        c = input("Alternativa C: ")
        d = input("Alternativa D: ")
        while True:
            gabarito = input("Gabarito: ").strip().upper()
            if gabarito in ["A","B","C","D"]:
                break
            else:
                
                print("Opção inválida, escolha uma alternativa entre A e D.")
        newquestion = {
        "pergunta" : pergunta,
        "a" : a,
        "b" : b,
        "c" : c,
        "d" : d,
        "gabarito" : gabarito}
        perguntas.append(newquestion)
        limpa()
    with open("perguntas.json", "w") as prgt:
        json.dump(perguntas, prgt, indent=4)
    tp = print("'perguntas.json' criado.\npress any key...")
    with open("perguntas.json", "r") as gb:
        perguntasx = json.load(gb)
    limpa()
qntddeperguntas = len(perguntasx)   
while True:
    try:
        qntdd = int(input(f"Quantas perguntas deseja responder? (Entre 1 e {qntddeperguntas})\n- "))
        if qntdd<=qntddeperguntas:
            break
        else:
            limpa()
            print(f"Existem apenas {qntddeperguntas} registradas. Tente novamente.")
            continue   
    except ValueError:
        limpa()
        print("Valor inválido.")

for i in range(1,4,1):
    limpa()
    print("iniciando em...")
    print(i)
    time.sleep(1)
gabaritoreal = []
gabaritousuario = []
for i in perguntasx:
    gabaritex = i["gabarito"]
    gabaritoreal.append(gabaritex)
print(" ====== PERGUNTAS ====== ")
random.shuffle(perguntasx)
for i, q in enumerate(perguntasx, start=1):
    if i > qntdd:
        break
    limpa()
    print(f"{i} - {q["pergunta"]}")
    print(f"A) - {q["a"]}")
    print(f"B) - {q["b"]}")
    print(f"C) - {q["c"]}")
    print(f"D) - {q["d"]}")
    while True:
        gabs = input("Alternativo correta : ").strip().upper()
        if gabs in ["A","B","C","D"]:
            gabaritousuario.append(gabs)
            break
        else:
            print("Opção inválida, escolha uma alternativa entre A e D.")
            continue
limpa()
pontos=0
for i in range(1,101,1):
    print("Carregando resultado...")
    print(i,"%")
    time.sleep(0.01)
    limpa()
for i,(gab, resp) in enumerate(zip(gabaritoreal, gabaritousuario)):
    if resp == gab:
        pontos+=1
        print(f"{i} - ✅ Resposta correta. (Seu Gabarito - {resp})")
    else:
        print(f"{i} - ❌ Resposta incorreta. (Seu Gabarito - {resp} | Gabarito correto - {gab})")
print(f"Pontos totais : {pontos}")
aproveitamento = (pontos/qntdd)*100
print(f"Aproveitamento : {aproveitamento}%")
try:
    with open("ranking.json", "r")as rnk:
        ranking = json.load(rnk)
except FileNotFoundError:
    ranking = []
jogador = {
    "id" : len(ranking)+1,
    "pontos" : pontos,
    "aproveitamento" : aproveitamento
}
ranking.append(jogador)
tp = input("press any key...")
limpa()
while True:
    try:
        sair = int(input("Escolha um opção\n<1> Ver Ranking\n<2> Apagar Perguntas/Respostas e Sair\n<3> Adicionar Questões\n\n<0> Salvar e Sair\n"))
        match sair:
            case 1:
                limpa()
                if len(ranking)!=0:
                    for i in ranking:
                        print(f"Id do Jogador: {i["id"]}")
                        print(f"Pontos: {i["pontos"]}")
                        print(f"Aproveitamento : {i["aproveitamento"]}%")
                        tm = input("press any key...")
                        limpa()
                    continue
                else:
                    limpa()
                    print("Sem progressos salvos.")
                    continue
            case 2:
                arquivo = "perguntas.json"
                os.remove(arquivo)
                limpa()
                print("Apagou e saiu.")
                break
            case 3:
                for i in range(qntd):
                        print(f"Questão {i+1} - ")
                        pergunta = input("Pergunta : ")
                        a = input("Alternativa A: ")
                        b = input("Alternativa B: ")
                        c = input("Alternativa C: ")
                        d = input("Alternativa D: ")
                        while True:
                            gabarito = input("Gabarito: ").strip().upper()
                            if gabarito in ["A","B","C","D"]:
                                break
                            else:
                                print("Opção inválida, escolha uma alternativa entre A e D.")
                        newquestion = {
                        "pergunta" : pergunta,
                        "a" : a,
                        "b" : b,
                        "c" : c,
                        "d" : d,
                        "gabarito" : gabarito}
                        perguntas.append(newquestion)
                break
            case 0:
                limpa()
                with open("ranking.json", "w") as arquive:
                    json.dump(ranking, arquive, ensure_ascii=False)
                print("saiu.")
                break
            case _:
                limpa()
                print("Valor Inválido.")
                continue
    except ValueError:
        limpa()
        print("Valor Inválido.")