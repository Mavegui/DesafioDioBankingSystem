#========================================================================================================================================
# Autor: Guilherme Feitosa Alves | Software Engineer | Back-End Developer | Python Developer 
# Data: 04/02/2025
#========================================================================================================================================
# Descrição: Sistema bancário simples, que realiza autenticação de usuários e permite depósitos, saques e exibição de extrato. 
# Desafio proposto pela Digital Innovation One em parceria com a Vivo no bootcamp "Coding The Future Vivo - Python AI Backend Developer"
#========================================================================================================================================

from datetime import datetime  # Biblioteca para manipulação de datas e horas
import re  # Biblioteca para expressões regulares

# ==========================
# FUNÇÕES DE VALIDAÇÃO
# ==========================
def validar_endereco(endereco):
    """Valida se o endereço segue o formato correto: Logradouro, Número - Bairro - Cidade/UF"""
    padrao = r"^([\w\s]+), (\d+) - ([\w\s]+) - ([\w\s]+)/([A-Z]{2})$"
    match = re.match(padrao, endereco)

    if not match:
        return False

    logradouro, numero, bairro, cidade, uf = match.groups()

    if not validar_numero(numero) or not validar_uf(uf):
        return False

    return True

def validar_cpf(cpf):
    """Verifica se o CPF contém exatamente 11 dígitos numéricos."""
    return cpf.isdigit() and len(cpf) == 11

def validar_nome(nome):
    """Verifica se o nome contém apenas letras e espaços."""
    return nome.replace(" ", "").isalpha()

def validar_numero(numero):
    """Verifica se o valor contém apenas números (exemplo: número da casa)."""
    return numero.isdigit()

def validar_uf(uf):
    """Verifica se a UF tem exatamente 2 letras maiúsculas."""
    return len(uf) == 2 and uf.isalpha()

def validar_data_nascimento(data_nascimento):
    """Verifica se a data de nascimento está no formato correto e se a pessoa tem 18+ anos."""
    try:
        data = datetime.strptime(data_nascimento, "%d/%m/%Y")
        idade = (datetime.now() - data).days // 365
        return idade >= 18
    except ValueError:
        return False

def validar_senha(senha, tamanho):
    """Verifica se a senha contém apenas números e tem o tamanho correto."""
    return senha.isdigit() and len(senha) == tamanho


# ==========================
# CLASSE USUÁRIO
# ==========================
class Usuario:
    def __init__(self, nome, cpf, data_nascimento, endereco):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco


# ==========================
# CLASSE CONTA CORRENTE
# ==========================
class ContaCorrente:
    agencia_padrao = "0001"
    limite_saque = 500
    max_saques_diarios = 3
    numero_contas = 0  # Número sequencial para contas

    def __init__(self, usuario, senha_4_digitos):
        ContaCorrente.numero_contas += 1
        self.agencia = ContaCorrente.agencia_padrao
        self.numero_conta = ContaCorrente.numero_contas
        self.usuario = usuario
        self.senha_4_digitos = senha_4_digitos
        self.saldo = 0.0
        self.extrato = []
        self.numero_saques = 0

    def depositar(self, saldo, valor, extrato, /):
        """Método para realizar um depósito. Usa argumentos Positional-Only."""
        if not isinstance(valor, (int, float)) or valor <= 0:
            print("\nErro: O valor do depósito deve ser um número positivo.")
            return saldo, extrato

        saldo += valor
        extrato.append(f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] Depósito: R$ {valor:.2f}")
        print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso!")
        return saldo, extrato

    def sacar(self, *, saldo, valor, extrato, limite, numero_saques, limite_saques):
        """Método para realizar um saque. Usa argumentos Keyword-Only."""
        if not isinstance(valor, (int, float)) or valor <= 0:
            print("\nErro: O valor do saque deve ser um número positivo.")
            return saldo, extrato, numero_saques

        if valor > saldo:
            print("\nErro: Saldo insuficiente.")
        elif valor > limite:
            print(f"\nErro: O valor do saque excede o limite de R$ {limite}.")
        elif numero_saques >= limite_saques:
            print("\nErro: Número máximo de saques diários excedido.")
        else:
            saldo -= valor
            numero_saques += 1
            extrato.append(f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] Saque: R$ {valor:.2f}")
            print(f"\nSaque de R$ {valor:.2f} realizado com sucesso!")

        return saldo, extrato, numero_saques

    def exibir_extrato(self, saldo, /, *, extrato):
        """Método para exibir o extrato. Usa Positional-Only e Keyword-Only."""
        horario_extrato = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print("\n================ EXTRATO ================")
        print(f"Cliente: {self.usuario.nome}")
        print(f"Agência: {self.agencia} | Conta: {self.numero_conta}")
        print(f"Data do Extrato: {horario_extrato}")
        print("-----------------------------------------")

        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            for transacao in extrato:
                print(transacao)

        print("-----------------------------------------")
        print(f"Saldo: R$ {saldo:.2f}")
        print("=========================================")


# ==========================
# CLASSE BANCO
# ==========================
class Banco:
    def __init__(self):
        self.usuarios = []
        self.contas = []

    def criar_usuario(self):
        print("\n=== Cadastro de Novo Usuário ===")

        while True:
            nome = input("Nome completo: ")
            if validar_nome(nome):
                break
            print("\nErro: Nome inválido! Digite apenas letras.")

        while True:
            data_nascimento = input("Data de nascimento (DD/MM/AAAA): ")
            if validar_data_nascimento(data_nascimento):
                break
            print("\nErro: Data de nascimento inválida ou usuário menor de 18 anos.")

        while True:
            cpf = input("CPF (somente números): ")
            if validar_cpf(cpf) and not any(usuario.cpf == cpf for usuario in self.usuarios):
                break
            print("\nErro: CPF inválido ou já cadastrado!")

        while True:
            endereco = input("Endereço (Logradouro, Número - Bairro - Cidade/UF): ")
            if validar_endereco(endereco):
                break
            print("\nErro: Endereço inválido! Use o formato correto: Rua Exemplo, 123 - Centro - Cidade/UF")

        novo_usuario = Usuario(nome, cpf, data_nascimento, endereco)
        self.usuarios.append(novo_usuario)
        print("\nUsuário cadastrado com sucesso!")

    def criar_conta(self):
        print("\n=== Cadastro de Nova Conta Corrente ===")

        cpf = input("Informe o CPF do titular da conta: ")
        usuario_encontrado = next((usuario for usuario in self.usuarios if usuario.cpf == cpf), None)

        if not usuario_encontrado:
            print("\nErro: Usuário não encontrado!")
            return

        while True:
            senha_4_digitos = input("Crie uma senha de 4 dígitos: ")
            if validar_senha(senha_4_digitos, 4):
                break
            print("\nErro: A senha deve ser somente números com limite de 4 dígitos!")

        nova_conta = ContaCorrente(usuario_encontrado, senha_4_digitos)
        self.contas.append(nova_conta)
        print(f"\nConta criada com sucesso! Agência: {nova_conta.agencia}, Conta: {nova_conta.numero_conta}")

    def acessar_conta(self):
        print("\n=== Acesso ao Sistema Bancário ===")

        cpf = input("Informe seu CPF: ")
        contas_usuario = [conta for conta in self.contas if conta.usuario.cpf == cpf]

        if not contas_usuario:
            print("\nErro: Nenhuma conta encontrada para este CPF.")
            return None

        print("\nSelecione uma conta:")
        for conta in contas_usuario:
            print(f"[{conta.numero_conta}] Agência: {conta.agencia} | Conta: {conta.numero_conta}")

        numero_conta = int(input("\nDigite o número da conta desejada: "))
        conta_selecionada = next((conta for conta in contas_usuario if conta.numero_conta == numero_conta), None)

        if not conta_selecionada:
            print("\nErro: Conta não encontrada!")
            return None

        for tentativa in range(3):
            senha_digitada = input("\nDigite a senha de 4 dígitos: ")
            if senha_digitada == conta_selecionada.senha_4_digitos:
                print(f"\nLogin realizado com sucesso! Bem-vindo, {conta_selecionada.usuario.nome}.\n")
                return conta_selecionada

            print(f"\nSenha incorreta! Tentativas restantes: {2 - tentativa}")

        print("\nErro: Número máximo de tentativas excedido!")
        return None

# ==========================
# MENUS USADOS
# ==========================
def menu_banco():
    """
    Função para exibir o menu principal de cadastro de usuários.
    """
  
    print("\n=== MENU PRINCIPAL ===")
    print("1. Criar Usuário")
    print("2. Criar Conta Corrente")
    print("3. Acessar Conta")
    print("4. Sair") 

def menu_operacoes():
    """
    Função para exibir o menu de operações bancárias.
    """
    print("\n=== Sistema Bancário ===")
    print("1. Depósito")
    print("2. Saque")
    print("3. Extrato")
    print("4. Sair")
  

# ==========================
# FUNÇÃO PRINCIPAL
# ==========================
def main():
    banco = Banco()

    while True:
        menu_banco()
        opcao = input("=> ")

        if opcao == "1":
            banco.criar_usuario()

        elif opcao == "2":
            banco.criar_conta()

        elif opcao == "3":
            conta = banco.acessar_conta()
            if conta:
                while True:
                    menu_operacoes()
                    opcao_banco = input("=> ")

                    if opcao_banco == "1":
                        valor = float(input("\nValor do depósito: "))
                        conta.saldo, conta.extrato = conta.depositar(conta.saldo, valor, conta.extrato)

                    elif opcao_banco == "2":
                        valor = float(input("\nValor do saque: "))
                        conta.saldo, conta.extrato, conta.numero_saques = conta.sacar(
                            saldo=conta.saldo, valor=valor, extrato=conta.extrato,
                            limite=conta.limite_saque, numero_saques=conta.numero_saques,
                            limite_saques=conta.max_saques_diarios
                        )

                    elif opcao_banco == "3":
                        conta.exibir_extrato(conta.saldo, extrato=conta.extrato)

                    elif opcao_banco == "4":
                        break

        elif opcao == "4":
            break

if __name__ == "__main__":
    main()