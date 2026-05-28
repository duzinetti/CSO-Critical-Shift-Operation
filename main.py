from models.pedidos import *
from models.entregadores import *
from validations.validations import *
from models.consults import (pedidos_pendentes, pedidos_entregues, buscar_pedido,
                              entregadores_disponiveis, entregas_por_entregador,
                              pedidos_por_cliente, pedidos_sem_entregador)
from models.reports import *

stats = {"total_pedidos": 0}
pedidos = {}
entregadores = {}

PRIORIDADES = ["ALTA", "NORMAL"]
STATUS = ["pendente", "em rota", "entregue", "cancelado"]
VEICULOS = ["carro", "van", "moto"]
MAX_PEDIDOS = 5


def menu_principal():
    print("\n" + "=" * 50)
    print("FLUXONORTE".center(50))
    print("=" * 50)
    print("1 - Cadastrar")
    print("2 - Atualizar Pedidos")
    print("3 - Consultar Informações")
    print("4 - Relatórios")
    print("0 - Sair")


def submenu_cadastro():
    print("\n" + "=" * 50)
    print("CADASTROS".center(50))
    print("=" * 50)
    print("1 - Cadastrar Pedido")
    print("2 - Cadastrar Entregador")
    print("0 - Voltar")


def submenu_atualizacao():
    print("\n" + "=" * 50)
    print("ATUALIZAÇÃO DE PEDIDOS".center(50))
    print("=" * 50)
    print("1 - Alterar Status")
    print("2 - Cancelar Pedido")
    print("3 - Associar Entregador")
    print("4 - Remover Entregador")
    print("5 - Alterar Disponibilidade do Entregador")
    print("0 - Voltar")


def submenu_consultas():
    print("\n" + "=" * 50)
    print("CONSULTAS".center(50))
    print("=" * 50)
    print("1 - Pedidos Pendentes")
    print("2 - Pedidos Entregues")
    print("3 - Buscar Pedido")
    print("4 - Entregadores Disponíveis")
    print("5 - Entregas por Entregador")
    print("6 - Pedidos por Cliente")
    print("7 - Pedidos sem Entregador")
    print("0 - Voltar")


def submenu_relatorios():
    print("\n" + "=" * 50)
    print("RELATÓRIOS".center(50))
    print("=" * 50)
    print("1 - Total de Pedidos")
    print("2 - Pedidos por Status")
    print("3 - Pedidos Prioridade Alta")
    print("4 - Entregador com Mais Entregas")
    print("0 - Voltar")


def resumo_ao_sair():
    print("\n" + "=" * 50)
    print("RESUMO DO TURNO".center(50))
    print("=" * 50)

    total = len(pedidos)
    entregues = sum(1 for p in pedidos.values() if p["status"] == "entregue")
    pendentes = sum(1 for p in pedidos.values() if p["status"] == "pendente")
    cancelados = sum(1 for p in pedidos.values() if p["status"] == "cancelado")
    em_rota = sum(1 for p in pedidos.values() if p["status"] == "em rota")
    sem_entregador = sum(1 for p in pedidos.values() if p["status"] == "pendente" and p["id_entregador"] == "")

    print(f"  Total de pedidos     : {total}")
    print(f"  Entregues            : {entregues}")
    print(f"  Em rota              : {em_rota}")
    print(f"  Pendentes            : {pendentes}")
    print(f"  Cancelados           : {cancelados}")
    print(f"  Sem entregador       : {sem_entregador}")
    print("=" * 50)
    print("\nSistema encerrado.")


def executar_menu():

    opc = ""

    while opc != "0":

        menu_principal()
        opc = input("Escolha uma opção: ").strip()

        match opc:

            case "1":

                sub = ""

                while sub != "0":

                    submenu_cadastro()
                    sub = input("Escolha: ").strip()

                    match sub:

                        case "1":
                            cadastrar_pedido(
                                pedidos,
                                entregadores,
                                PRIORIDADES,
                                stats
                            )

                        case "2":
                            cadastrar_entregador(
                                entregadores,
                                VEICULOS
                            )

                        case "0":
                            pass

                        case _:
                            print("[ERRO] Opção inválida.")

            case "2":

                sub = ""

                while sub != "0":

                    submenu_atualizacao()
                    sub = input("Escolha: ").strip()

                    match sub:

                        case "1":
                            alterar_status(
                                pedidos,
                                STATUS
                            )

                        case "2":
                            cancelar_pedido(
                                pedidos,
                                entregadores
                            )

                        case "3":
                            associar_entregador(
                                pedidos,
                                entregadores,
                                MAX_PEDIDOS
                            )

                        case "4":
                            remover_entregador(
                                pedidos,
                                entregadores
                            )

                        case "5":
                            alterar_disponibilidade(entregadores)

                        case "0":
                            pass

                        case _:
                            print("[ERRO] Opção inválida.")

            case "3":

                sub = ""

                while sub != "0":

                    submenu_consultas()
                    sub = input("Escolha: ").strip()

                    match sub:

                        case "1":
                            pedidos_pendentes(pedidos)

                        case "2":
                            pedidos_entregues(pedidos)

                        case "3":
                            buscar_pedido(pedidos)

                        case "4":
                            entregadores_disponiveis(entregadores)

                        case "5":
                            entregas_por_entregador(pedidos, entregadores)

                        case "6":
                            pedidos_por_cliente(pedidos)

                        case "7":
                            pedidos_sem_entregador(pedidos)

                        case "0":
                            pass

                        case _:
                            print("[ERRO] Opção inválida.")

            case "4":

                sub = ""

                while sub != "0":

                    submenu_relatorios()
                    sub = input("Escolha: ").strip()

                    match sub:

                        case "1":
                            total_pedidos(stats)

                        case "2":
                            pedidos_por_status(pedidos, STATUS)

                        case "3":
                            pedidos_alta_prioridade(pedidos)

                        case "4":
                            entregador_mais_entregas(pedidos, entregadores)

                        case "0":
                            pass

                        case _:
                            print("[ERRO] Opção inválida.")

            case "0":
                resumo_ao_sair()

            case _:
                print("\n[ERRO] Opção inválida.")


executar_menu()