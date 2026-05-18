"""Cadastro de Pedidos
Permite a inserção de novos pedidos, que devem possuir as seguintes informações:
• ID do pedido (deve iniciar por uma letra e conter quatro valores numéricos)
• Nome do Cliente
• Endereço
• Prioridade (Alta, Normal)
• Descrição do Pedido
• Status do Pedido (Pendente, Em Rota, Entregue, Cancelado)
• ID do Entregador"""

def cadastrar_pedido(id_pedido,nome_cliente,endereco,prioridade,descricao_pedido,status_pedido,id_entregador):
    pedidos = {}
    

    