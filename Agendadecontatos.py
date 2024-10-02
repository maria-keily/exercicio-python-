import os # modulo os fornece funções par a interagir com o sistema operacional

#função carrega arquivos de contatos se tiver algum
def carregar_contatos():
    contatos = {}
    if os.path.exists("contatos.txt"):
        with open("contatos,txt", "r") as arquivo:
            for linha in arquivo: #adicionar os contatos em uma linha 
                nome, telefone, email = linha.strip().split(",")

      return contatos # retornar a lista 

#salvar contatos em um arquivo temporário
def salvar_contatos(contatos):
    with open("contatos.txt," "W") as arquivo:
        for nome, dados in contatos.items():
            arquivo.write(f"{nome};{dados['telefone']};{dados['email']}\n")

#função adicionar um contato
def adicionar_contatos(contatos):
    nome = input("Digite o nome do contato: ")   
    telefone = input("Digite o telefone: ") 
    email = input("Digite o email: ")
    contatos[nome] = {"telefone": telefone, "email": email}  
    print(f"Contato {nome} adicionado com sucesso!")


#função para remover um contato 
def remove_contato(contatos):
    nome = input("Digite o nome do contato a ser removido: ")
    del contatos [nome] 
    print(f"Contato {nome} removido com sucesso!")
 else:#se não tiver,não faz nada
  print("Contato não encontrado. ")


#função para atualizar um contato
def atualizar_contato(contatos):
  nome = input("Digite o novo telefone: ")
if nome in contatos:
    telefone = input("Digite o novo telefone: ")
    email = input("Digite o novo email: ")
    contatos[nome] = {"telefone": telefone, "email": email}  
    print(f"Contatos {nome} atualizado com sucesso!")
else:
  print("Nenhum contato cadastrado.")      

  #função para exibir todos os contatos
  def exibir_contatos(contatos):
if contatos:
    for nome, dados in contatos.items():
        print(f"Nome: {Nome}, telefone: {dados['telefone']}, email: {dados['email']}")
    else:
        print("Nenhum contato cadastrado.")    

#menu principal
def menu():
 contatos = carregar_contatos()

  while True: #while estrutura de loop infinito 
    print("\n. 1. Adicionar contato")
    print("2. Remover contato")
    print("3. Exibir contato0")
    print("4. Sair")
    
    
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        adicionar_contatos(contatos)
    elif opcao == "2":
        remove_contato(contatos)
    elif opcao == "3":
        atualizar_contato(contatos)
    elif opcao == "4":
        exibir_contatos(contatos)
    elif opcao == "5"
        salvar_contatos(contatos)
        print("Contatos salvos. Saindo do programa.")
        break
     else:
        print("Opção inválida, tente novamente.")

#executa o menu principal

       if_name__== "_main_":
        menu()           
