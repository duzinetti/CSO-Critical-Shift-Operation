from validations.validations import *


def cadastrar_entregador(entregadores, VEICULOS):

    print("\n─── Cadastro de Entregador ───")

    id_e = input("  ID do entregador (4 dígitos): ").strip()

    if not id_entregador_valido(id_e):
        print("  [ERRO] ID inválido.")
        return

    if id_e in entregadores:
        print("  [ERRO] Entregador já cadastrado.")
        return

    nome = input("  Nome: ").strip()

    if not nao_vazio(nome, "Nome"):
        return

    print("  Veículos: moto, carro, van")

    veiculo = input("  Veículo: ").strip().lower()

    if veiculo not in VEICULOS:
        print("  [ERRO] Veículo inválido.")
        return

    disp = input("  Disponível? (s/n): ").strip().lower()

    if disp not in ["s", "n"]:
        print("  [ERRO] Responda s ou n.")
        return

    entregadores[id_e] = {
        "id": id_e,
        "nome": nome,
        "veiculo": veiculo,
        "pedidos": [],
        "disponivel": disp == "s"
    }

    print(f"  [OK] Entregador {id_e} cadastrado.")


def associar_entregador(pedidos, entregadores, MAX_PEDIDOS):

    id_p = input("  ID do pedido: ").strip().upper()

    if id_p not in pedidos:
        print("  [ERRO] Pedido não encontrado.")
        return

    if pedidos[id_p]["status"] in ["cancelado", "entregue"]:
        print("  [AVISO] Pedido não aceita entregador.")
        return

    id_e = input("  ID do entregador: ").strip()

    if not id_entregador_valido(id_e):
        print("  [ERRO] ID inválido.")
        return

    if id_e not in entregadores:
        print("  [ERRO] Entregador não cadastrado.")
        return

    if not entregadores[id_e]["disponivel"]:
        print("  [AVISO] Entregador indisponível.")
        return

    ativos = 0

    for p in entregadores[id_e]["pedidos"]:

        if pedidos[p]["status"] not in ["cancelado", "entregue"]:
            ativos += 1

    if ativos >= MAX_PEDIDOS:
        print("  [AVISO] Limite de pedidos atingido.")
        return

    id_atual = pedidos[id_p]["id_entregador"]

    if id_atual in entregadores:

        if id_p in entregadores[id_atual]["pedidos"]:
            entregadores[id_atual]["pedidos"].remove(id_p)

    pedidos[id_p]["id_entregador"] = id_e

    entregadores[id_e]["pedidos"].append(id_p)

    print(f"  [OK] Entregador {id_e} associado ao pedido {id_p}.")


def remover_entregador(pedidos, entregadores):

    id_p = input("  ID do pedido: ").strip().upper()

    if id_p not in pedidos:
        print("  [ERRO] Pedido não encontrado.")
        return

    id_e = pedidos[id_p]["id_entregador"]

    if id_e == "":
        print("  [AVISO] Nenhum entregador associado.")
        return

    if id_e in entregadores:
        entregadores[id_e]["pedidos"].remove(id_p)

    pedidos[id_p]["id_entregador"] = ""

    print(f"  [OK] Entregador removido do pedido {id_p}.")

