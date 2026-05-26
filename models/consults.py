#consultas

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
    if id_p not in pedidos:
        print("  [ERRO] Pedido não encontrado.")
        return
    p = pedidos[id_p]
    print(f"  ID         : {p['id']}")
    print(f"  Cliente    : {p['cliente']}")
    print(f"  Endereço   : {p['endereco']}")
    print(f"  Prioridade : {p['prioridade']}")
    print(f"  Status     : {p['status']}")
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