#========================================================================================================================================
# Autor: Guilherme Feitosa Alves | Software Engineer | Back-End Developer | Python Developer 
# Data: 27/01/2025
#========================================================================================================================================
# Descrição: Sistema bancário simples, que realiza autenticação de usuários e permite depósitos, saques e exibição de extrato. 
# Desafio proposto pela Digital Innovation One em parceria com a Vivo no bootcamp "Coding The Future Vivo - Python AI Backend Developer"
#========================================================================================================================================

# Import necessário para data e hora
from datetime import datetime 


class Usuario:
    """
    Classe que representa um usuário do sistema bancário.
    
    Cada usuário possui uma conta associada e precisa autenticar-se usando agência, conta e senha.
    Neste código, a autenticação é feita com base em uma lista contendo 2 usuários pré-cadastrados.
    """
    def __init__(self, nome, agencia, conta, senha):
        #Inicializa os atributos do usuário
        self.nome = nome
        self.agencia = agencia
        self.conta = conta
        self.senha = senha
        self.conta_bancaria = ContaBancaria()

    def __str__(self):
        #Retorna uma representação em string do usuário
        return f"Usuário: {self.nome}, Agência: {self.agencia}, Conta: {self.conta}"


class ContaBancaria:
    """
    Classe que representa uma conta bancária.

    Atributos:
        saldo (float): Armazena o saldo atual da conta.
        limite_saque (float): Limite máximo para cada saque.
        numero_saques (int): Número de saques realizados no dia.
        transacoes (list): Lista que registra o histórico de transações.

    Métodos:
        depositar(valor): Adiciona um valor ao saldo e registra a transação.
        sacar(valor): Retira um valor do saldo, respeitando os limites.
        exibir_extrato(nome_cliente, agencia, conta): Exibe o extrato detalhado com transações e saldo.
    """
    LIMITE_SAQUES = 3

    def __init__(self):
        #Inicializa os atributos da conta bancária
        self.saldo = 0
        self.limite_saque = 500
        self.numero_saques = 0
        self.transacoes = []  # Lista para armazenar o histórico de transações

    def depositar(self, valor):
        """
        Método para exibir o depositar no formato solicitado.
        """
        if valor > 0:
            self.saldo += valor
            horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            self.transacoes.append(f"[{horario}] Depósito: R$ {valor:.2f}")
            print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("\nErro: O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        """
        Método para sacar no formato solicitado.
        """
        if valor > self.saldo:
            print("\nErro: Saldo insuficiente.")
        elif valor > self.limite_saque:
            print(f"\nErro: O valor do saque excede o limite de R$ {self.limite_saque}.")
        elif self.numero_saques >= self.LIMITE_SAQUES:
            print("\nErro: Número máximo de saques diários excedido.")
        elif valor <= 0:
            print("\nErro: O valor do saque deve ser positivo.")
        else:
            self.saldo -= valor
            self.numero_saques += 1
            horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            self.transacoes.append(f"[{horario}] Saque: R$ {valor:.2f}")
            print(f"\nSaque de R$ {valor:.2f} realizado com sucesso!")
    
    def exibir_extrato(self, nome_cliente, agencia, conta):
        """
        Método para exibir o extrato no formato solicitado.
        """
        horario_extrato = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print("\n================ EXTRATO ================")
        print(f"Cliente: {nome_cliente}")
        print(f"Agência: {agencia} Conta: {conta}")
        print(f"Data do Extrato: {horario_extrato}")
        print("-----------------------------------------")
        
        if not self.transacoes:
            print("Não foram realizadas movimentações.")
        else:
            for transacao in self.transacoes:
                print(transacao)
        
        print("-----------------------------------------")
        print(f"Saldo: R$ {self.saldo:.2f}")
        print("=========================================")


# Lista de usuários cadastrados para autenticação (agência, conta e senha)
usuarios = [
    Usuario("Gui", "0001", "12345-6", "1234"),
    Usuario("Faah", "0001", "67890-1", "5678")
]


def autenticar(agencia, conta, senha):
    """
    Função para autenticar o usuário com base na agência, conta e senha.
    """
    for usuario in usuarios:
        if usuario.agencia == agencia and usuario.conta == conta and usuario.senha == senha:
            return usuario
    return None


def exibir_menu():
    """
    Função para exibir o menu de opções.
    """
    print("\n=== Sistema Bancário ===")
    print("1. Depósito")
    print("2. Saque")
    print("3. Extrato")
    print("4. Sair")

def main():
    """
    Função principal do sistema bancário.

    - Solicita as credenciais do usuário.
    - Realiza a autenticação.
    - Exibe o menu de operações (depósito, saque, extrato, sair).
    - Processa as opções do usuário e executa as operações correspondentes.
    """
    agencia = input("Informe sua agência: ")
    conta = input("Informe sua conta: ")
    senha = input("Informe sua senha (4 dígitos): ")

    # Autentica o usuário com base nas credenciais fornecidas
    usuario_autenticado = autenticar(agencia, conta, senha)

    if usuario_autenticado:
        print(f"\nLogin bem-sucedido! Bem-vindo, {usuario_autenticado.nome}.")
   
        while True:
            # Exibe o menu de operações
            exibir_menu()
            opcao = input("=> ").lower()

            # Processa a opção escolhida
            if opcao == "1":
                try:
                    valor = float(input("\nDigite o valor do depósito: "))
                    usuario_autenticado.conta_bancaria.depositar(valor)
                except ValueError:
                    print("\nErro: Insira um valor numérico válido.")

            elif opcao == "2":
                try:
                    valor = float(input("\nDigite o valor do saque: "))
                    usuario_autenticado.conta_bancaria.sacar(valor)
                except ValueError:
                    print("\nErro: Insira um valor numérico válido.")

            elif opcao == "3":
                usuario_autenticado.conta_bancaria.exibir_extrato(
                    usuario_autenticado.nome, usuario_autenticado.agencia, usuario_autenticado.conta
                )

            elif opcao == "4":
                print(f"\nAté logo, {usuario_autenticado.nome}! Obrigado por usar o Sistema Bancário.")
                break

            else:
                print("\nOpção inválida. Tente novamente.")
                
    else:
        print("\nErro: Agência, conta ou senha inválidos.")
 
if __name__ == "__main__":
    main()