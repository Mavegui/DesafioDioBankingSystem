# **Desafio DIO | Sistema Bancário em Python 🏦**

Este repositório contém o desafio proposto pela **Digital Innovation One (DIO)** em parceria com a **Vivo**, no bootcamp "**Coding The Future Vivo - Python AI Backend Developer**".
O objetivo do projeto é criar um **sistema bancário** funcional utilizando as práticas de Programação Orientada a Objetos.

---

## **📝 Descrição do Projeto**

O desafio tem como foco consolidar os conhecimentos adquiridos durante o bootcamp. Ele engloba a implementação prática de:

- **Introdução à Programação Orientada a Objetos (POO)** em Python.
- **Aprendendo o Conceito de Herança**.
- **Aplicando Encapsulamento**.
- **Conhecendo Polimorfismo**.
- **Interfaces e  Classes Abstratas**.
- **Modelando o Sistema Bancário em POO com Python**.

Além disso, o projeto foi ampliado com recursos extras, como:

- **Programação Orientada a Objetos (POO):** Estruturando o sistema em classes para maior organização e reutilização de código.
- **Documentação do Código:** Código bem comentado, explicando cada etapa e funcionalidade.
- **Uso da biblioteca datetime:** Para registrar a data e hora de todas as transações e extratos.
- **Uso da biblioteca re:** Para realizar validação de entrada de dados em endereço.
- **Uso da biblioteca ABC:** Biblioteca para trabalhar com classes abstratas em Python.

---

## **🚀 Funcionalidades**

O sistema bancário possui as seguintes funcionalidades:

1. Criação do usuário e conta corrente:
    - O cliente acessa o sistema e cria seu usuário e conta corrente.

2. Login com autenticação:
    - O cliente acessa sua conta informando **número da conta** e **senha**.

3. Depósito:
    - Aceita apenas valores positivos.
    - Atualiza o saldo e registra no histórico da transação.

4. Saque:
    - Limite máximo de saque por transação: R$500.00.
    - Máximo de 3 saques diários.
    - Registra a transação no histórico.

5. Extrato:
    - Exibe o nome do cliente, agência, conta, e a data de emissão do extrato.
    - Lista todas as transações realizadas (depósitos e saques), incluindo data e hora.
    - Mostra o saldo final da conta no rodapé.

6. Mensagens amigáveis:
    - O sistema informa claramente o status de cada operação, incluindo erros como saldo insuficiente ou limite de saques atingido.

---

## 📋 Requisitos

Para executar o projeto, você precisará de:

- **Python 3.8 ou superior** instalado no seu sistema.
- Um terminal ou IDE (como **VSCode**).

---

## ▶️ Como Executar o Sistema

- **Clone o repositório:**

```bash
git clone https://github.com/Mavegui/DesafioDioBankingSystem.git
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

1. **Criação de usuário**

    - Criação do usuário no sistema.
    - Exemplo de criação:
    ```bash
    === Cadastro de Novo Usuário ===
    Nome completo: Gui Feitosa
    Data de nascimento (DD/MM/AAAA): 18/10/2001
    CPF (somente números): 12345678911
    Logradouro: Eucalipto
    Número da casa: 135
    Bairro: Padre Cícero
    Cidade: Milagres
    Sigla do Estado (UF): CE

    Usuário cadastrado com sucesso!
    ```

2. **Criação de conta**

    - Criação da conta corrente.
    - Exemplo de criação:
    ```bash
    === Cadastro de Nova Conta Corrente ===
    Informe o CPF do titular da conta: 12345678911
    Crie uma senha de 4 dígitos: 1234

    Conta criada com sucesso! Agência: 0001, Conta: 1
    ```

3. **Login**

    - Informe seu cpf, conta e senha cadastrados.
    - Exemplo do login:
    ```bash
    === Acesso ao Sistema Bancário ===
    Informe seu CPF: 12345678911

    Contas encontradas:
    Agência: 0001 | Conta: 1

    Informe a Agência: 0001

    Informe o Número da conta: 1

    Informe sua Senha de 4 dígitos: 1234

    Login realizado com sucesso! Bem-vindo, Gui Feitosa.
    ```

4. **Depósito**

    - Digite o valor desejado para depósito.
    - Exemplo de saída:
    ```bash
    Digite o valor do depósito: 200
    Depósito de R$ 200.00 realizado com sucesso!
    ```
5. **Saque**

    - Insira o valor para saque (respeitando o limite de R$500.00 e o saldo disponível).
    - Exemplo de saída:
    ```bash
    Digite o valor do saque: 100
    Saque de R$ 100.00 realizado com sucesso!
    ```

6. **Extrato**

   - Visualize o extrato completo:
   ```bash
   ================== EXTRATO ==================
   Cliente: Gui
   Agência: 0001 Conta: 1
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

- **Guilherme Feitosa | [Portfólio](https://www.porfoliogui.com.br/)**

