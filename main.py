from models.pedidos import *
print("="*50)
print("MENU PRINCIPAL".center(50))
print("="*50)
print("1- Cadastrar Pedidos")
print("2- Cadastrar de Entregadores ")
print("3- Atualizar Pedidos")
print("4- Consultar Informações")
print("5- Relatórios Operacionais")
opc = int(input("Digite a opção desejada:"))

match opc:
    case 1:
       cadastrar_pedido()
    
    case 2: 
        pass
    
    case 3: 
        print("="*50)
        print("ATUALIZAÇÃO DOS PEDIDOS".center(50))
        print("="*50)
        print("1- Alterar Status do Pedido")
        print("2- Cancelar Pedido")
        print("3- Associar Entregadores a Pedidos")
        print("4- Remover associação de Entregador")


    case 4: 
        print("="*50)
        print("CONSULTAR INFORMAÇÕES".center(50))
        print("="*50)
        print("Pedidos Pendentes")
        print("Pedidos Entregues")
        print("Buscar Pedido por ID")
        print("Entregador Disponível")
        print("Entregas por Entregador")


    case 5: 
        print("="*50)
        print("RELATÓRIOS OPERACIONAIS".center(50))
        print("="*50)
        print("Total de Pedidos")
        print("Quantidade de Pedidos por Status")
        print("Pedidos com Alta Prioridade")
        print("Entregador com Maior Número de Entregas")
        




