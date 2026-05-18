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


