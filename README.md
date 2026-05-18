# 🚚 CSO - Critical Shift Operation 

> Sistema operacional de gerenciamento de entregas urbanas desenvolvido em Python puro.  
> Projeto Avaliativo A2 — Disciplina: APPC (Prática) — Engenharia de Software — PUC Campinas 2026

---

## 📋 Índice

- [Equipe](#equipe)
- [Sobre o Projeto](#sobre-o-projeto)
- [Funcionalidades](#funcionalidades)
- [Decisões de Implementação](#decisões-de-implementação)
- [Estrutura de Dados](#estrutura-de-dados)
- [Como Executar](#como-executar)
- [Estrutura do Menu](#estrutura-do-menu)
- [Regras de Negócio](#regras-de-negócio)

---

## 👥 Equipe

| Nome | RA |
|---|---|
| *Eduardo Zinetti* | *26003681* |
| *(Nome do Aluno 2)* | *(RA)* |
| *(Nome do Aluno 3)* | *(RA)* |

---

## 📌 Sobre o Projeto

A **FluxoNorte** é uma empresa de logística urbana que enfrentava problemas sérios no controle de suas entregas: informações espalhadas em planilhas, registros manuais inconsistentes e ausência de um fluxo centralizado de operação.

Este sistema foi desenvolvido como um **protótipo operacional em Python** para auxiliar na organização diária da empresa, permitindo o cadastro, atualização, consulta e geração de relatórios sobre pedidos e entregadores — tudo via terminal, sem banco de dados ou interface gráfica.

---

## ✅ Funcionalidades

### 📦 Cadastro de Pedidos
- Inserção de novos pedidos com validação de ID (`letra + 4 números`, ex: `A1234`)
- Campos: ID, nome do cliente, endereço, prioridade (Alta/Normal), descrição, status e entregador

### 🧑‍💼 Cadastro de Entregadores
- Inserção de entregadores com validação de ID (exatamente 4 dígitos)
- Campos: ID, nome, veículo (carro/van/moto), pedidos associados e disponibilidade
- Não permite duplicidade de entregadores

### 🔄 Atualização de Pedidos
- Alterar status do pedido seguindo sequência lógica: `Pendente → Em Rota → Entregue`
- Cancelar pedido
- Reativar pedido cancelado (retorna para status `Pendente`)
- Associar entregador a um pedido
- Remover associação de entregador

### 🔍 Consultas
- Listar pedidos pendentes
- Listar pedidos entregues
- Buscar pedido por ID
- Listar entregadores disponíveis
- Ver todas as entregas realizadas por um entregador

### 📊 Relatórios Operacionais
- Total de pedidos cadastrados
- Quantidade de pedidos por status
- Pedidos com Alta Prioridade
- Entregador com maior número de entregas
- Histórico de operações do turno (log)
- Detecção automática de inconsistências

### 🔚 Encerramento de Turno
- Exibe relatório completo do turno
- Detecta e lista inconsistências nos dados
- Opção de limpar dados ou manter para o próximo turno

---

## 🧠 Decisões de Implementação

| Decisão | Escolha | Justificativa |
|---|---|---|
| **Ordem de entrega** | Prioridade Alta primeiro, depois ordem de chegada | Mais realista operacionalmente; pedidos urgentes não podem esperar |
| **Limite de pedidos por entregador** | Por tipo de veículo (moto: 2, carro: 4, van: 6) | Capacidade de carga varia por veículo; evita sobrecarga |
| **Reativação de cancelados** | Permitida, retorna para "Pendente" | Erros de operação são comuns; sistema deve ser tolerante |
| **Reordenação automática** | Sim, ao cadastrar pedido de Alta prioridade | Garante que urgências sejam tratadas imediatamente |
| **Sequência de status** | Obrigatória (Pendente → Em Rota → Entregue) | Evita inconsistências; pedido não pode ser "Entregue" sem passar por "Em Rota" |

---

## 🗂️ Estrutura de Dados

O sistema utiliza **listas de dicionários** como estrutura principal de armazenamento em memória.

```python
# Pedido
{
  "id": "A1001",
  "cliente": "João Silva",
  "endereco": "Rua das Flores, 42",
  "prioridade": "Alta",          # "Alta" ou "Normal"
  "descricao": "Caixa frágil",
  "status": "Pendente",          # Pendente | Em Rota | Entregue | Cancelado
  "id_entregador": None,
  "cancelado_antes": False       # Flag para controle de reativação
}

# Entregador
{
  "id": "0021",
  "nome": "Carlos Souza",
  "veiculo": "moto",             # "moto" | "carro" | "van"
  "pedidos": ["A1001"],          # Lista de IDs de pedidos associados
  "disponivel": True
}

# Log de operações
log = [
  "10:32 - Pedido A1001 cadastrado",
  "10:35 - Entregador 0021 associado ao pedido A1001",
  "10:40 - Status do pedido A1001 alterado para Em Rota"
]
```

---

## ▶️ Como Executar

### Pré-requisitos
- Python 3.x instalado ([python.org](https://www.python.org/downloads/))
- Nenhuma biblioteca externa necessária

### Execução via IDLE (Python.org)
```
1. Abra o IDLE do Python
2. Vá em File > Open
3. Selecione o arquivo main.py
4. Pressione F5 para executar
```

### Execução via VSCode
```
1. Abra a pasta do projeto no VSCode
2. Selecione o arquivo main.py
3. Pressione o botão ▶ (Run) ou use o terminal:
   python main.py
```

### Execução via Terminal
```bash
python main.py
```

> ⚠️ **Atenção:** O sistema roda inteiramente no terminal. Todos os dados são armazenados em memória e serão perdidos ao encerrar o programa (a menos que o turno seja salvo).

---

## 🗺️ Estrutura do Menu

```
============================================
       FLUXONORTE — OPERAÇÃO TURNO CRÍTICO
============================================

[1] Cadastro de Pedidos
[2] Cadastro de Entregadores
[3] Atualização de Pedidos
[4] Consultas
[5] Relatórios Operacionais
[6] Encerramento de Turno
[0] Sair

--------------------------------------------
[3] Atualização de Pedidos
  [3.1] Alterar status do pedido
  [3.2] Cancelar pedido
  [3.3] Reativar pedido cancelado
  [3.4] Associar entregador a pedido
  [3.5] Remover entregador de pedido

--------------------------------------------
[4] Consultas
  [4.1] Pedidos pendentes
  [4.2] Pedidos entregues
  [4.3] Buscar pedido por ID
  [4.4] Entregadores disponíveis
  [4.5] Entregas realizadas por entregador

--------------------------------------------
[5] Relatórios Operacionais
  [5.1] Total de pedidos
  [5.2] Pedidos por status
  [5.3] Pedidos de Alta Prioridade
  [5.4] Entregador com mais entregas
  [5.5] Log de operações do turno
  [5.6] Detectar inconsistências
```

---

## 📏 Regras de Negócio

- **ID de Pedido:** deve iniciar com uma letra maiúscula seguida de exatamente 4 dígitos numéricos (ex: `A1234`, `B0099`)
- **ID de Entregador:** deve conter exatamente 4 dígitos numéricos (ex: `0021`, `1042`)
- **Limite de pedidos por entregador:**
  - 🏍️ Moto → máximo **2 pedidos**
  - 🚗 Carro → máximo **4 pedidos**
  - 🚐 Van → máximo **6 pedidos**
- **Sequência de status obrigatória:** `Pendente → Em Rota → Entregue`
- **Pedido cancelado** pode ser reativado; retorna para `Pendente`
- **Entregador indisponível** não pode ser associado a novos pedidos
- **Não é permitido** cadastrar dois entregadores com o mesmo ID
- **Reordenação automática:** ao cadastrar pedido de Alta prioridade, a fila é reorganizada

---

> Curso: Engenharia de Software — PUC Campinas  
> Disciplina: Algoritmos de Programação, Projetos e Computação (APPC) — Prática  
> Período: 2026

---
---

# 🚚 Operation Critical Shift — FluxoNorte

> Urban delivery management operational system developed in pure Python.  
> Evaluative Project A2 — Course: APPC (Practice) — Software Engineering — PUC Campinas 2026

---

## 👥 Team

| Name | Student ID |
|---|---|
| *Eduardo Zinetti* | *26003681* |
| *(Student 2)* | *(ID)* |
| *(Student 3)* | *(ID)* |
| *(Student 4)* | *(ID)* |

---

## 📌 About the Project

**FluxoNorte** is an urban logistics company that faced serious problems in delivery control: information scattered across spreadsheets, inconsistent manual records, and no centralized operational flow.

This system was developed as an **operational prototype in Python** to assist in the company's daily organization, enabling registration, updating, querying, and report generation for orders and delivery personnel — all via terminal, without databases or graphical interfaces.

---

## ✅ Features

- **Order Registration** — with ID validation (`letter + 4 digits`)
- **Delivery Personnel Registration** — with duplication prevention and ID validation
- **Order Updates** — status changes, cancellations, reactivation, driver assignment
- **Queries** — pending/delivered orders, search by ID, available drivers
- **Operational Reports** — totals, by status, high priority, top performer, log, inconsistency detection
- **Shift Closing** — full shift report with option to clear or keep data

---

## ▶️ How to Run

### Requirements
- Python 3.x ([python.org](https://www.python.org/downloads/))
- No external libraries required

```bash
python main.py
```

Compatible with **IDLE (Python.org)** and **VSCode**.

---

## 📏 Business Rules

- **Order ID:** one uppercase letter + exactly 4 digits (e.g. `A1234`)
- **Driver ID:** exactly 4 digits (e.g. `0021`)
- **Order limit per driver:** Motorcycle: 2 / Car: 4 / Van: 6
- **Status sequence:** `Pending → In Transit → Delivered`
- Cancelled orders **can be reactivated** back to `Pending`
- Unavailable drivers **cannot** be assigned to new orders
- Duplicate driver IDs are **not allowed**

---


> Software Engineering — PUC Campinas | APPC Practice | 2026