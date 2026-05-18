def cadastrar_pedido(id_pedido,nome_cliente,endereco,prioridade,descricao_pedido,status_pedido,id_entregador):
    pedidos = {}
    pedidos[id_pedido] = [nome_cliente,endereco,prioridade,descricao_pedido,status_pedido,id_entregador]


def cadastrar_entregador(id_entregador,nome_entregador,veiculo,id_pedido_entregar,disponibilidade):
    entregadores = {}
    entregadores[id_entregador] = [nome_entregador,veiculo,id_pedido_entregar,disponibilidade]


    