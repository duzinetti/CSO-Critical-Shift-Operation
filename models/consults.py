from validations.validations import id_pedido_valido, id_entregador_valido


def pedidos_pendentes(pedidos):
    print("\n─── Pedidos Pendentes ───")
    lista = [p for p in pedidos.values() if p["status"] == "pendente"]
    if not lista:
        print("  Nenhum pedido pendente.")
        return
    for p in lista:
        print(f"  {p['id']} | {p['cliente']} | {p['prioridade']} | Entregador: {p['id_entregador'] or 'Sem entregador'}")
    print(f"  Total: {len(lista)}")


def pedidos_entregues(pedidos):
    print("\n─── Pedidos Entregues ───")
    lista = [p for p in pedidos.values() if p["status"] == "entregue"]
    if not lista:
        print("  Nenhum pedido entregue.")
        return
    for p in lista:
        print(f"  {p['id']} | {p['cliente']} | Entregador: {p['id_entregador'] or 'Sem entregador'}")
    print(f"  Total: {len(lista)}")


def buscar_pedido(pedidos):
    print("\n─── Buscar Pedido ───")
    id_p = input("  ID do pedido: ").strip().upper()

    if not id_pedido_valido(id_p):
        return

    if id_p not in pedidos:
        print("  [ERRO] Pedido não encontrado.")
        return

    p = pedidos[id_p]
    historico = " → ".join(p.get("historico", [p["status"]]))

    print(f"  ID         : {p['id']}")
    print(f"  Cliente    : {p['cliente']}")
    print(f"  Endereço   : {p['endereco']}")
    print(f"  Prioridade : {p['prioridade']}")
    print(f"  Status     : {p['status']}")
    print(f"  Histórico  : {historico}")
    print(f"  Descrição  : {p['descricao']}")
    print(f"  Peso       : {p.get('peso', '—')} kg")
    print(f"  Frágil     : {'Sim' if p.get('fragil') else 'Não'}")
    print(f"  Veículo    : {p.get('veiculo_ideal', '—')}")
    print(f"  Entregador : {p['id_entregador'] or 'Sem entregador'}")


def entregadores_disponiveis(entregadores):
    print("\n─── Entregadores Disponíveis ───")
    lista = [e for e in entregadores.values() if e["disponivel"]]
    if not lista:
        print("  Nenhum entregador disponível.")
        return
    for e in lista:
        print(f"  {e['id']} | {e['nome']} | {e['veiculo']} | Pedidos: {len(e['pedidos'])}")
    print(f"  Total: {len(lista)}")


def entregas_por_entregador(pedidos, entregadores):
    print("\n─── Entregas por Entregador ───")
    id_e = input("  ID do entregador: ").strip()

    if not id_entregador_valido(id_e):
        return

    if id_e not in entregadores:
        print("  [ERRO] Entregador não encontrado.")
        return

    e = entregadores[id_e]
    entregues = [pedidos[p] for p in e["pedidos"] if p in pedidos and pedidos[p]["status"] == "entregue"]

    print(f"  Entregador : {e['nome']} ({e['id']}) | {e['veiculo']}")
    print(f"  ─────────────────────────────────")

    if not entregues:
        print("  Nenhuma entrega concluída.")
        return

    for p in entregues:
        print(f"  {p['id']} | {p['cliente']} | {p['endereco']}")

    print(f"  Total entregue: {len(entregues)}")


def pedidos_por_cliente(pedidos):
    print("\n─── Pedidos por Cliente ───")
    nome = input("  Nome do cliente: ").strip()

    if nome == "":
        print("  [ERRO] Nome não pode ser vazio.")
        return

    lista = [p for p in pedidos.values() if p["cliente"].lower() == nome.lower()]

    if not lista:
        print(f"  Nenhum pedido encontrado para '{nome}'.")
        return

    for p in lista:
        print(f"  {p['id']} | {p['prioridade']} | Status: {p['status']} | Entregador: {p['id_entregador'] or 'Sem entregador'}")

    print(f"  Total: {len(lista)}")


def pedidos_sem_entregador(pedidos):
    print("\n─── Pedidos Pendentes sem Entregador ───")
    lista = [
        p for p in pedidos.values()
        if p["status"] == "pendente" and p["id_entregador"] == ""
    ]

    if not lista:
        print("  Todos os pedidos pendentes têm entregador associado.")
        return

    for p in lista:
        print(f"  {p['id']} | {p['cliente']} | {p['prioridade']} | Veículo ideal: {p.get('veiculo_ideal', '—')}")

    print(f"  Total: {len(lista)}")