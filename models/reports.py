def total_pedidos(stats):
    print(f"\n  Total de pedidos cadastrados: {stats['total_pedidos']}")


def pedidos_por_status(pedidos, STATUS):
    status_count = {}
    for p in pedidos.values():
        status = p["status"]
        status_count[status] = status_count.get(status, 0) + 1

    print("\n  Pedidos por status:")

    for st, count in status_count.items():
        print(f"    {st}: {count}")


def pedidos_alta_prioridade(pedidos):
    print("\n  Pedidos de alta prioridade:")
    encontrou = False
    for p in pedidos.values():
        if p["prioridade"] == "ALTA":
            encontrou = True
            print(f"\n   ID: {p['id']} | Cliente: {p['cliente']} | Status: {p['status']}")
    if not encontrou:
        print("    Nenhum pedido de alta prioridade.")


def entregador_mais_entregas(pedidos, entregadores):
    entregas_count = {}
    ativos_count = {}

    for e_id, e in entregadores.items():
        ativos_count[e_id] = sum(
            1 for p in e["pedidos"]
            if pedidos.get(p, {}).get("status") not in ["cancelado", "entregue"]
        )

    for p in pedidos.values():
        if p["status"] == "entregue" and p["id_entregador"] != "":
            e_id = p["id_entregador"]
            entregas_count[e_id] = entregas_count.get(e_id, 0) + 1

    if not entregas_count:
        print("\n  Nenhuma entrega registrada.")
        return

    max_entregas = max(entregas_count.values())
    top_entregadores = [e_id for e_id, count in entregas_count.items() if count == max_entregas]

    print("\n  Entregador(es) com mais entregas:")
    for e_id in top_entregadores:
        nome = entregadores[e_id]["nome"] if e_id in entregadores else "Desconhecido"
        ativos = ativos_count.get(e_id, 0)
        print(f"    {nome} (ID: {e_id}) | Entregas concluídas: {max_entregas} | Pedidos ativos: {ativos}")