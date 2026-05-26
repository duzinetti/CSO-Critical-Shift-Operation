# ════════════════════════════════════════════════════════════
#  VALIDAÇÕES
# ════════════════════════════════════════════════════════════
""" 
Os ids seguem o padrão:
    PEDIDO - 5 caracteres: 1 letra + 4 números (ex: P1234)
    ENTREGADOR - 4 caracteres: apenas números (ex: 1234)
    
"""
def id_pedido_valido(id_pedido):
    if len(id_pedido) == 5 and id_pedido[0].isalpha() and id_pedido[1:].isdigit():
        return True
    else:
        print("ID do pedido deve conter 5 caracteres, começando com uma letra seguida de 4 números.")
        return False

def id_entregador_valido(id_entregador):
    if len(id_entregador) == 4 and id_entregador.isdigit():
        return True
    else:
        print("ID do entregador deve conter 4 caracteres numéricos.")
        return False

def nao_vazio(valor, campo):
    resultado = valor.strip() != ""
    if not resultado:
        print(f"  [ERRO] '{campo}' não pode ser vazio.")
    return resultado

def peso_valido(valor_str):
    valor_str = valor_str.replace(",", ".")
    if not valor_str.replace(".", "", 1).isdigit():
        print("  [ERRO] Peso deve ser um número positivo (ex: 3.5).")
        return None
    peso = float(valor_str)
    if peso <= 0:
        print("  [ERRO] Peso deve ser um número positivo (ex: 3.5).")
        return None
    return peso

def veiculo_por_peso_fragilidade(peso, fragil):
    # Frágil nunca vai de moto
    if fragil:
        if peso <= 20:
            return "carro"
        return "van"
    if peso <= 5:
        return "moto"
    if peso <= 20:
        return "carro"
    return "van"