from models.pedidos import *
opc = 1
while opc <= 6 and opc >=1 :

        print("="*50)
        print("MENU PRINCIPAL".center(50))
        print("="*50)
        print("1- Cadastrar Pedidos")
        print("2- Cadastrar de Entregadores ")
        print("3- Atualizar Pedidos")
        print("4- Consultar Informações")
        print("5- Relatórios Operacionais")
        print("6- Finalizar Sistema")
        opc = int(input("Digite a opção desejada:"))

        match opc:
            case 1:
                  print("-"*25,"CADASTRAR PEDIDO","-"*25)
                  id_pedido = int(input("ID do Pedido: "))
                  nome_cliente = input("Insira o nome do Cliente: ")
                  endereco = input("Insira o endereço de entrega: ")
                  print("-"*25,"PRIORIDADES","-"*25)
                  print("1 - Entrega Normal")
                  print("2 - Entrega Rapida")
                  print("3 - Entrega Urgente")
                  prioridade = int(input("Insira a prioridade: "))
                  descricao_pedido = input("Insira a descrição do produto:")
                  print("-"*25,"STATUS","-"*25)
                  print("1 - Pendente")
                  print("2 - Em rota")
                  print("3 - Entregue")
                  print("4 - Cancelado")
                  status_pedido = int(input("Insira o status: "))
                  id_entregador = int(input("Insira a identificação do entregador: "))
                  cadastrar_pedido(id_pedido,nome_cliente,endereco,prioridade,descricao_pedido,status_pedido,id_entregador)
            
            case 2: 
                print("-"*25,"CADASTRAR ENTREGADOR","-"*25)
                id_enregador = int(input("ID do Entregador"))
                nome_entregador = input("Insira o nome do entregador: ")
                print("-"*25,"VEÍCULO","-"*25)
                print("1 - Moto")
                print("2 - Carro")
                print("3 - Van")
                print("4 - Caminhāo")
                veiculo = int(input("Insira o veículo do entregador: "))
                id_pedido_entregar = int(input("ID do pedido a ser entregue: "))
                disponibilidade = input("Disponível ou não - True/False: ")
                cadastrar_entregador(id_entregador,nome_entregador,veiculo,id_pedido_entregar,disponibilidade)
            
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
            case 6:
                  break
else: 
     print("Opção inválida!")



