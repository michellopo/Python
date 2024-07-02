import textwrap

def menu():
    Menu = """\n
    =======MENU========

    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tLista Contas
    [nu]\tNovo Usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(Menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0 :
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n!!!! Operação negada. Valor inválido. !!!!")

    return saldo, extrato   
    
    
def sacar(*, saldo, valor, extrato, limite, numero_saque, limite_saque):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = numero_saque >= limite_saque

    if excedeu_saldo:
        print("\n!!! Operação falhou! Você não tem saldo suficiente.!!!")
    elif excedeu_limite:
        print("\n!!! Operação falhou! O valor do saque excede o limite.!!!")
    elif excedeu_saque:
        print("\n!!! Operação falhou! Quantidade de saques excedido.!!!")
    elif valor > 0:
                saldo -= valor 
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saque += 1
                print ("\n=== Saque realizado com sucesso. ===")
    else:
                print("Operação falhou, valor invalido para deposito.")

def exibir_extrato(saldo, /, *, extrato):
      print ("\n ======= EXTRATO =======")
      print ("Não fora realizada movimentações." if not extrato else extrato)
      print (f"\nSaldo:\t\tR$ {saldo:.2f}")
      print ("================================")

def cria_usuario(usuarios):
     cpf = input("Informe seu CPF (somente números): ")
     usuario = filtrar_usuario(cpf, usuarios)

     if usuario: 
          print ("\n!!!! Usuário existente !!!!")
          return
     
     nome = input("Informe o nome completo: ")
     data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
     endereco = input("Informe o endereço (logradouro, nr - bairro - cidade/Estado): ")

     usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereço": endereco})

     print ("=== Usuário criado com sucesso. ===")

def filtrar_usuario(cpf, usuarios):
     usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf ] 
     return usuarios_filtrados[0] if usuarios_filtrados else None  

def criar_conta(agencia, numero_conta, usuarios):
     cpf = input("Informe o CPF do usuário: ")
     usuario = filtrar_usuario(cpf, usuarios)

     if usuario:
          print ("\n=== Conta criada com sucesso. ===")
          return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
     
     print ("\n!!!! Usuário não encontrado, processo encerrado. !!!!")

def listar_contas(contas):
     for conta in contas:
          linha = f"""\
          Agência:\t{conta['agencia']}
          C\C:\t\t{conta['numero_conta']}
          Titular:\t{conta['usuario']['nome']}
          """
          print("=" * 100)
          print(textwrap.dedent(linha))

def main():

    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saque = 0
    usuarios = []
    contas = []

    while True:

        opcao= menu()

        if opcao == "d":
            valor = float(input("Informe o valor do deposito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor de saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saque=numero_saque,
                limite_saque=LIMITE_SAQUES,

            )

        elif opcao == "e":
           exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
             cria_usuario(usuarios)

        elif opcao == "nc":
             numero_conta = len(contas) + 1
             conta = criar_conta(AGENCIA, numero_conta, usuarios)

             if conta: 
                  contas.append(conta)
        
        elif opcao == "lc":
             listar_contas(contas)


        elif opcao == "q":
            print("Sair")
            break

        else:
            print("Operação invalida, por favor selecione a operação desejada.")

main()