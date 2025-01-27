# **Desafio DIO | Sistema Bancário em Python 🏦**

Este repositório contém o desafio proposto pela **Digital Innovation One (DIO)** em parceria com a **Vivo**, no bootcamp "**Coding The Future Vivo - Python AI Backend Developer**".
O objetivo do projeto é criar um **sistema bancário** funcional com as operações básicas: saque, depósito e extrato, seguindo os requisitos mínimos definidos.

---

## **📝 Descrição do Projeto**

O desafio tem como foco consolidar os conhecimentos adquiridos durante o bootcamp. Ele engloba a implementação prática de:

- **Estruturação do código** em Python.
- **Uso de operadores** e manipulação de strings.
- **Estruturas condicionais e de repetição**.

Além disso, o projeto foi ampliado com recursos extras, como:

- **Programação Orientada a Objetos (POO):** Estruturando o sistema em classes para maior organização e reutilização de código.
- **Documentação do Código:** Código bem comentado, explicando cada etapa e funcionalidade.
- **Uso da biblioteca datetime:** Para registrar a data e hora de todas as transações e extratos.

---

## **🚀 Funcionalidades**

O sistema bancário possui as seguintes funcionalidades:

1. Login com autenticação:

    -O cliente acessa sua conta informando **agência**, **número da conta** e **senha**.

2. Depósito:

    -Aceita apenas valores positivos.
    -Atualiza o saldo e registra a transação com data e hora.

3. Saque:

    -Limite máximo de saque por transação: R$500.00.
    -Máximo de 3 saques diários.
    -Registra a transação com data e hora.

4. Extrato:

    -Exibe o nome do cliente, agência, conta, e a data de emissão do extrato.
    -Lista todas as transações realizadas (depósitos e saques), incluindo data e hora.
    -Mostra o saldo final da conta no rodapé.

5. Mensagens amigáveis:

    -O sistema informa claramente o status de cada operação, incluindo erros como saldo insuficiente ou limite de saques atingido.

---

## 📋 Requisitos

Para executar o projeto, você precisará de:

-**Python 3.8 ou superior** instalado no seu sistema.
-Um terminal ou IDE (como **VSCode**, **PyCharm** ou **Jupyter Notebook**) para executar o código.

---

## ▶️ Como Executar o Sistema

- **Clone o repositório:**

```bash
https://github.com/Mavegui/DesafioDioBankingSystem.git
```

- **Navegue até a pasta do projeto:**

```bash
cd DesafioDioBankingSystem
```

- **Execute o programa:**

```bash
python3 DesafioBankingSystem.py
```

--- 

## **📚 Exemplo de Uso**

1. **Login**

    -Informe sua agência, conta e senha cadastrados.
    -Exemplo de usuários:
    ```bash
    usuarios = [
        Usuario("Gui", "0001", "12345-6", "1234"),
        Usuario("Faah", "0001", "67890-1", "5678")
    ]
    ```

2. **Depósito**

    -Digite o valor desejado para depósito.
    -Exemplo de saída:
    ```bash
    Digite o valor do depósito: 200
    Depósito de R$ 200.00 realizado com sucesso!
    ```
3. **Saque**

    -Insira o valor para saque (respeitando o limite de R$500.00 e o saldo disponível).
    -Exemplo de saída:
    ```bash
    Digite o valor do saque: 100
    Saque de R$ 100.00 realizado com sucesso!
    ```

4. **Extrato**

   -Visualize o extrato completo:
   ```bash
   ================== EXTRATO ==================
   Cliente: Gui
   Agência: 0001 Conta: 12345-6
   Data do Extrato: 24/01/2025 17:00:00
   --------------------------------------------
   [24/01/2025 16:30:00] Depósito: R$ 200.00
   [24/01/2025 16:45:00] Saque: R$ 100.00
   --------------------------------------------
   Saldo: R$ 100.00
   ============================================
   ```

---

## **✍️ Autor**

### Guilherme Feitosa | Software Engineer | Desenvolvedor Back-End
