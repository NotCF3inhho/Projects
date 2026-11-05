import os,time,random
def limpa():
    os.system("cls" if os.name == "nt" else "clear")
caracteres = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9",]
while True:
    limpa()
    usuario = input("Digite o seu username : ")
    senha = input("Digite a sua senha : ")
    senhaminusculo = senha.lower()
    print(f"Iniciando sistema BRUTE FORCE",end="")
    for i in range(3,0,-1):
        print(".",end="", flush=True)
        time.sleep(0.3)
    limpa()
    print("Alvo Definido",end="")
    time.sleep(1)
    for i in range(10):
        time.sleep(0.3)
        print(".",end="", flush=True)
    print()

    tentativas = 0
    inicio = time.time()
    found = False
    while not found:
        tentativas_random = random.choices(caracteres, k=len(senhaminusculo))
        tentativa = "".join(tentativas_random)
        tentativas+=1
        print(tentativa,end=" ")
        if tentativas % 50 == 0:
            print()
        if tentativa == senhaminusculo:
            found = True
            fim = time.time()
            tempo_gasto = fim - inicio
            print()
            print("SUCCESS!!!")
            print(f"Usuário : {usuario}")
            print(f"Senha : {senha}")
            print(f"Tentativas : {tentativas}")
            print(f"Tempo : {tempo_gasto}")
    t = input("Press any key...")
    limpa()
    for i in range(3,0,-1):
        limpa()
        print(f"Reiniciando em {i}...")
        time.sleep(1)
    


    
