saldo =0  # Saldo inicial
extrato = {}  # Dicionário para armazenar os depósitos
contador_transacoes = 1  # Contador para organizar os depósitos no dicionário
numero_saques = 0 
LIMITE_SAQUES =3

def exibir_menu(): #menu
    """Exibe o menu de opções para o usuário."""
    print("\nMenu:")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Extrato")
    print("4. Sair")

def deposito():
    """Realiza um depósito e armazena no extrato."""
    global saldo, contador_transacoes # Permite modificar as variáveis globais dentro da função
    
    try: # tratar  exceções
        valor = float(input("Digite o valor do depósito: "))
        if valor > 0:
            saldo += valor  # Atualiza o saldo
            extrato[f"Depósito {contador_transacoes}"] = f"+ R$ {valor:.2f}"  # Armazena no dicionário
            contador_transacoes += 1  # Incrementa o contador de transações
            
            print(f"O depósito de R$ {valor:.2f} foi realizado com sucesso!")
            print(f"Saldo atualizado: R$ {saldo:.2f}")
        else:
            print("Erro: O valor precisa ser positivo.")
    except ValueError: #se ocorrer algum erro
        print("Erro: Digite um número válido.")


def sacar ():
    global saldo, contador_transacoes ,LIMITE_SAQUES , numero_saques
    try: # tratar  exceções 
        valor =float(input('Digite o valor do saque :'))
        if  valor >  saldo : #Valor não pode ser maior que o saldo
            print ('Valor insulficiente')
        elif valor > 500 : #limite de saque 500
            print ('Limite de saque R$ 500 , digite outro valor : ')
        elif numero_saques >=LIMITE_SAQUES : #Limite 3 saques por dia
            print ('Só  e permitido fazer 3 saques por dia.')
        else:
            saldo = saldo - valor 
            extrato [f'Saque {contador_transacoes}'] = f'- R$ {valor:.2f}'
            contador_transacoes+=1 #adiciona quantas transações foram efetuadas para cada operação
            numero_saques+=1 #incrementa o numero de saques 
            #extrato.append(f"Saque: +R$ {valor:.2f}")  # Adiciona ao extrato
            print(f"O Saque de R$ {valor:.2f} foi realizado com sucesso!")
            print(f"Saldo atualizado: R$ {saldo:.2f}")
            
    except ValueError : # se ocorrer algum erro  
            print("Erro: Digite um número válido.")




while True :

    exibir_menu()
    escolha = int(input('Escolha uma opção : '))
    if escolha == 1 :
            deposito ()

    elif escolha == 2 :
            sacar ()
    
    elif escolha == 3 :
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
    
    elif escolha == 4 :
        print ('Saindo ..... Obrigado por usar o nosso  banco ,  Tenha uma  Boa tarde !') 
    else :
        print ('Opção invalida, tente novamente.')
        



