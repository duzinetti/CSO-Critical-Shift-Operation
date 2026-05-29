from validations.validations import *


def _chave_ordenacao(p):
    if p["prioridade"] == "ALTA":
        prioridade_num = 0
    else:
        prioridade_num = 1
    return (prioridade_num, p.get("ordem", 0))


def _menor_fila(e):
    return len(e["pedidos"])


def cadastrar_pedido(pedidos, entregadores, PRIORIDADES, stats):

    print("\n─── Cadastro de Pedido ───")

    id_sugerido = gerar_id_pedido(pedidos)
    print(f"  ID sugerido automaticamente: {id_sugerido}")
    escolha = input("  Pressione ENTER para aceitar ou digite um ID personalizado: ").strip().upper()

    if escolha == "":
        id_p = id_sugerido
    else:
        if not id_pedido_valido(escolha):
            return
        if escolha in pedidos:
            print("  [ERRO] Pedido já existe.")
            return
        id_p = escolha

    cliente = input("  Nome do cliente: ").strip()

    if not nao_vazio(cliente, "Nome do cliente"):
        return

    if not so_letras(cliente, "Nome do cliente"):
        return

    endereco = input("  Endereço: ").strip()

    if not nao_vazio(endereco, "Endereço"):
        return

    print("  Prioridades: ALTA, NORMAL")
    prioridade = input("  Prioridade: ").strip().upper()

    if prioridade not in PRIORIDADES:
        print("  [ERRO] Prioridade inválida. Digite ALTA ou NORMAL.")
        return

    descricao = input("  Descrição: ").strip()

    if not nao_vazio(descricao, "Descrição"):
        return

    peso_str = input("  Peso do pedido (kg, ex: 3.5): ").strip()
    peso = peso_valido(peso_str)

    if peso is None:
        return

    fragil_inp = input("  Pedido é frágil? (s/n): ").strip().lower()

    if fragil_inp not in ["s", "n"]:
        print("  [ERRO] Responda s ou n.")
        return

    fragil = fragil_inp == "s"

    veiculo_ideal = veiculo_por_peso_fragilidade(peso, fragil)
    print(f"  [INFO] Veículo ideal para este pedido: {veiculo_ideal.upper()}")

    pedidos[id_p] = {
        "id": id_p,
        "cliente": cliente,
        "endereco": endereco,
        "prioridade": prioridade,
        "descricao": descricao,
        "status": "pendente",
        "id_entregador": "",
        "peso": peso,
        "fragil": fragil,
        "veiculo_ideal": veiculo_ideal,
        "historico": ["pendente"],
        "ordem": stats["total_pedidos"]
    }

    candidatos = []

    for e in entregadores.values():
        if e["veiculo"] == veiculo_ideal and e["disponivel"]:
            candidatos.append(e)

    candidatos.sort(key=_menor_fila)

    if candidatos:
        escolhido = candidatos[0]
        pedidos[id_p]["id_entregador"] = escolhido["id"]
        escolhido["pedidos"].append(id_p)
        print(f"  [OK] Pedido {id_p} cadastrado e distribuído para o entregador {escolhido['id']} ({veiculo_ideal}).")
    else:
        print(f"  [OK] Pedido {id_p} cadastrado.")
        print(f"  [AVISO] Nenhum entregador de '{veiculo_ideal}' disponível. Associe manualmente.")

    stats["total_pedidos"] += 1


def alterar_status(pedidos, STATUS):

    id_p = input("  ID do pedido: ").strip().upper()

    if not id_pedido_valido(id_p):
        return

    if id_p not in pedidos:
        print("  [ERRO] Pedido não encontrado.")
        return

    if pedidos[id_p]["status"] == "cancelado":
        print("  [AVISO] Pedido cancelado não pode ser alterado.")
        return

    print("  Status disponíveis: pendente, em rota, entregue")
    novo = input("  Novo status: ").strip().lower()

    if novo not in STATUS:
        print("  [ERRO] Status inválido. Digite: pendente, em rota ou entregue.")
        return

    pedidos[id_p]["status"] = novo
    pedidos[id_p]["historico"].append(novo)

    print(f"  [OK] Status atualizado para '{novo}'.")


def cancelar_pedido(pedidos, entregadores):

    id_p = input("  ID do pedido: ").strip().upper()

    if not id_pedido_valido(id_p):
        return

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

    confirma = input(f"  Confirma o cancelamento do pedido {id_p}? (s/n): ").strip().lower()

    if confirma not in ["s", "n"]:
        print("  [ERRO] Responda s ou n.")
        return

    if confirma != "s":
        print("  [INFO] Cancelamento abortado.")
        return

    pedidos[id_p]["status"] = "cancelado"
    pedidos[id_p]["historico"].append("cancelado")

    id_ent = pedidos[id_p]["id_entregador"]

    if id_ent in entregadores:
        entregadores[id_ent]["pedidos"].remove(id_p)

    pedidos[id_p]["id_entregador"] = ""

    print(f"  [OK] Pedido {id_p} cancelado.")