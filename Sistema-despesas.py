import os 
os.system('clear')

def mostrarmenu():
    print("----------------------------------------")
    print("                  MENU")               
    print("----------------------------------------")
    print("              1 - Leitura")
    print("              2 - Adição")
    print("              3 - Deleção")
    print("              4 - Atualização")
    print("              5 - Categorias")
    print("              6 - Estatísticas")
    print("\nSelecione uma opção:")

def realizar_leitura():
    print("Opção de leitura selecionada")
    print("----------------------------------------------------------")
    print("\tNome\t\tCategoria\t     Valor")
    print("----------------------------------------------------------")
    with open("banco.csv", "r") as f:
        for linha in f:
            nome, categoria, valor = linha.split(";")
            print(f"\t{nome.strip()}\t\t{categoria.strip()}\t\t     R${valor.strip()}")

def realizar_adicao():
    print("Opção de adição selecionada")
    nomeadicao = input("O que você deseja que seja adicionado?").upper()
    categoriaadicao = input("Em qual categoria essa coisa se encaixa?").upper()
    valoradicao = input("Quanto custou?")
    with open("banco.csv", "a") as f:
        f.write(f"{nomeadicao};{categoriaadicao};{valoradicao}\n")
        print(f"{nomeadicao} adicionado com sucesso!")

def realizar_delecao():
    print("Opção de deleção selecionada")
    nomedelecao = input("O que você deseja que seja removido?").upper()
    item_encontrado = False  
    with open("banco.csv", "r") as f:
        linhas = f.readlines()
    with open("banco.csv", "w") as f:
        for linha in linhas:
            if not linha.startswith(nomedelecao + ";"):
                f.write(linha)
            
            else:
                item_encontrado = True
                print(f"{nomedelecao} removido com sucesso!")
    
    if not item_encontrado:
        print("O item não existe no banco.")

def realizar_atualizacao():
    print("Opção de atualização selecionada")
    nomeatualizacao = input("O que você deseja atualizar?").upper()
    item_encontrado = False
    with open("banco.csv", "r") as f:
        linhas = f.readlines()
    with open("banco.csv", "w") as f:
        for linha in linhas:
            if linha.startswith(nomeatualizacao + ";"):
                novacategoria = input("Qual a nova categoria?").upper()
                novovalor = input("Qual o novo valor?")
                f.write(f"{nomeatualizacao};{novacategoria};{novovalor}\n")
                item_encontrado = True
                print(f"{nomeatualizacao} atualizado com sucesso!")
            else:
               f.write(linha)

    if not item_encontrado:
        print("O item não existe no banco.")

def realizar_categoria():
    print("Opção de exibição por categoria selecionada")
    categoria_escolhida= input("Digite a categoria que deseja exibir: ").upper()
    print("----------------------------------------------------------")
    print("\tNome\t\tCategoria\t     Valor")
    print("----------------------------------------------------------")
    with open("banco.csv", "r") as f:
        for linha in f:
            nome, categoria, valor = linha.split(";")
            if categoria.strip() == categoria_escolhida:
                print(f"\t{nome.strip()}\t\t{categoria.strip()}\t\t     R${valor.strip()}")

def realizar_estatisticas():
    print("Opção de cálculo de média selecionada")
    valores = []
    with open("banco.csv", "r") as f:
        for linha in f:
            nome, categoria, valor = linha.split(";")
            valores.append(float(valor.strip()))
    
    if valores:
        media = sum(valores) / len(valores)
        total = sum(valores)
        print(f"A média dos valores registrados é: R${media:.2f}")
        print(f"O total dos valores registrados é: R${total}")
    else:
        print("Nenhum valor encontrado no banco.")
        
    categorias = {}
    total = 0

    with open("banco.csv", "r") as f:
        for linha in f:
            nome, categoria, valor = linha.split(";")
            valor = float(valor.strip())
            total += valor
            if categoria in categorias:
                categorias[categoria] += valor
            else:
                categorias[categoria] = valor
    
    print("Porcentagem por Categoria:")
    for categoria, valor_da_categoria in categorias.items():
        porcentagem = (valor_da_categoria / total) * 100
        print(f"{categoria}: {porcentagem:.2f}%")


def menu():
    opcao = input(f"\nDeseja iniciar o menu? (S/N): ")
    
    if opcao.upper() == "S":
        while True:
            mostrarmenu()
            opcao = input().upper()
            
            if opcao == "1":
                realizar_leitura()
                break
            elif opcao == "2":
                realizar_adicao()
                break
            elif opcao == "3":
                realizar_delecao()
                break
            elif opcao == "4":
                realizar_atualizacao()
                break
            elif opcao == "5":
                realizar_categoria()
                break
            elif opcao == "6":
                realizar_estatisticas()
                break
            else:
                print("Opção inválida!")
                print("Digite uma opção válida")
    elif opcao.upper() == "N":
        print("Programa encerrado.")
        return
    else:
        print("Opção inválida!")
        print("Digite uma opção válida")
        
    menu()

menu()