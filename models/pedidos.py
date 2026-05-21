
from validations.validations import *


def cadastrar_pedido(pedidos, entregadores, PRIORIDADES):

    print("\n─── Cadastro de Pedido ───")

    id_p = input("  ID do pedido (1 letra + 4 números): ").strip().upper()

    if not id_pedido_valido(id_p):
        print("  [ERRO] ID inválido.")
        return

    if id_p in pedidos:
        print("  [ERRO] Pedido já existe.")
        return

    cliente = input("  Nome do cliente: ").strip()

    if not nao_vazio(cliente, "Nome do cliente"):
        return

    endereco = input("  Endereço: ").strip()

    if not nao_vazio(endereco, "Endereço"):
        return

    print("  Prioridades: ALTA, NORMAL")

    prioridade = input("  Prioridade: ").strip().upper()

    if prioridade not in PRIORIDADES:
        print("  [ERRO] Prioridade inválida.")
        return

    descricao = input("  Descrição: ").strip()

    if not nao_vazio(descricao, "Descrição"):
        return

    id_ent = input("  ID do entregador (vazio para depois): ").strip()

    if id_ent != "":

        if not id_entregador_valido(id_ent):
            print("  [ERRO] ID inválido.")
            return

        if id_ent not in entregadores:
            print("  [ERRO] Entregador não cadastrado.")
            return

    pedidos[id_p] = {
        "id": id_p,
        "cliente": cliente,
        "endereco": endereco,
        "prioridade": prioridade,
        "descricao": descricao,
        "status": "pendente",
        "id_entregador": id_ent
    }

    if id_ent != "":
        entregadores[id_ent]["pedidos"].append(id_p)

    print(f"  [OK] Pedido {id_p} cadastrado.")


def alterar_status(pedidos, STATUS):

    id_p = input("  ID do pedido: ").strip().upper()

    if id_p not in pedidos:
        print("  [ERRO] Pedido não encontrado.")
        return

    if pedidos[id_p]["status"] == "cancelado":
        print("  [AVISO] Pedido cancelado não pode ser alterado.")
        return

    print("  Status disponíveis: pendente, em rota, entregue")

    novo = input("  Novo status: ").strip().lower()

    if novo not in STATUS:
        print("  [ERRO] Status inválido.")
        return

    pedidos[id_p]["status"] = novo

    print(f"  [OK] Status atualizado para '{novo}'.")


def cancelar_pedido(pedidos, entregadores):

    id_p = input("  ID do pedido: ").strip().upper()

    if id_p not in pedidos:
        print("  [ERRO] Pedido não encontrado.")
        return

    st = pedidos[id_p]["status"]

    msgs = {
        "cancelado": "Pedido já cancelado.",
        "entregue": "Pedido entregue não pode ser cancelado."
    }

    if st in msgs:
        print(f"  [AVISO] {msgs[st]}")
        return

    pedidos[id_p]["status"] = "cancelado"

    id_ent = pedidos[id_p]["id_entregador"]

    if id_ent in entregadores:
        entregadores[id_ent]["pedidos"].remove(id_p)

    pedidos[id_p]["id_entregador"] = ""

    print(f"  [OK] Pedido {id_p} cancelado.")

