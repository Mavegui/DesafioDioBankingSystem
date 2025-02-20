#========================================================================================================================================
# Autor: Guilherme Feitosa Alves | Software Engineer | Back-End Developer | Python Developer 
# Data: 20/02/2025
#========================================================================================================================================
# Descrição: Sistema bancário orientado a objetos
# Aborda cadastro de usuários, criação de contas correntes, depósitos, saques e historico de transações. 
# Desafio proposto pela Digital Innovation One em parceria com a Vivo no bootcamp "Coding The Future Vivo - Python AI Backend Developer"
#========================================================================================================================================

from datetime import datetime # Biblioteca para manipulação de datas e horas
from abc import ABC, abstractmethod # Biblioteca para classes abstratas
import re # Biblioteca para expressões regulares

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
# CLASSES ABSTRATAS
# ==========================
class Pessoa(ABC):
    """ 
    Classe abstrata para representar uma pessoa.
    
    Atributos protegidos (_atributo):
    - _nome: Nome completo da pessoa.
    - _cpf: CPF da pessoa (apenas números).
    - _data_nascimento: Data de nascimento no formato "DD/MM/AAAA".
    - _endereco: Endereço completo no formato "Logradouro, Número - Bairro - Cidade/UF".
    
    Uso do @property:
    - Permite acessar os atributos de forma segura, sem expô-los diretamente.
    - Mantém o princípio do encapsulamento, evitando modificações diretas.
    """
    
    def __init__(self, nome, cpf, data_nascimento, endereco):
        """Inicializa uma pessoa com nome, CPF, data de nascimento e endereço."""
        self._nome = nome
        self._cpf = cpf
        self._data_nascimento = data_nascimento
        self._endereco = endereco

    @property
    def nome(self):
        """Retorna o nome da pessoa."""
        return self._nome

    @property
    def cpf(self):
        """Retorna o CPF da pessoa."""
        return self._cpf

    @property
    def data_nascimento(self):
        """Retorna a data de nascimento da pessoa."""
        return self._data_nascimento

    @property
    def endereco(self):
        """Retorna o endereço pessoa."""
        return self._endereco

class Conta(ABC):
    """ 
    Classe abstrata para representar uma conta bancária.
    
    Atributos de classe:
    - agencia_padrao: Define a agência padrão como "0001".
    - numero_contas: Contador para atribuir um número único a cada conta criada.
    
    Atributos protegidos (_atributo):
    - _agencia: Armazena a agência da conta (fixa como "0001").
    - _numero_conta: Número único da conta, incrementado automaticamente.
    - _usuario: Referência ao objeto do usuário (titular da conta).
    - _senha_4_digitos: Senha numérica de 4 dígitos para acessar a conta.
    - _saldo: Valor disponível na conta bancária.
    - _historico: Objeto da classe Historico para armazenar as transações da conta.

    Métodos:
    - validar_senha(senha): Verifica se a senha informada corresponde à senha cadastrada.
    - realizar_transacao(transacao): Executa e registra uma transação na conta.
    - exibir_extrato(): Exibe o extrato das transações realizadas na conta.
    """
    
    agencia_padrao = "0001"
    numero_contas = 0

    def __init__(self, usuario, senha_4_digitos):
        """Inicializa uma conta garantindo que a senha tenha exatamente 4 dígitos numéricos."""
        while not validar_senha(senha_4_digitos, tamanho=4):
            print("Senha inválida. A senha deve conter exatamente 4 dígitos numéricos.")
            senha_4_digitos = input("Crie uma senha de 4 dígitos: ")
        
        Conta.numero_contas += 1
        self._agencia = Conta.agencia_padrao
        self._numero_conta = Conta.numero_contas
        self._usuario = usuario
        self._senha_4_digitos = senha_4_digitos
        self._saldo = 0.0
        self._historico = Historico()

    @property
    def saldo(self):
        return self._saldo
    
    @property
    def agencia(self):
        return self._agencia

    @property
    def numero_conta(self):
        return self._numero_conta

    def validar_senha(self, senha):
        """Verifica se a senha informada está correta."""
        return self._senha_4_digitos == senha

    def realizar_transacao(self, transacao):
        """Executa uma transação e a registra no histórico da conta."""
        transacao.registrar(self)

    def exibir_extrato(self):
        """Exibe todas as transações realizadas na conta, além do saldo atual."""
        print("\n================ EXTRATO ================")
        print(f"Cliente: {self._usuario.nome}")
        print(f"Agência: {self._agencia} | Conta: {self._numero_conta}")
        print(f"Data do Extrato: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print("-----------------------------------------")
        
        if not self._historico.transacoes:
            print("Não foram realizadas movimentações.")
        else:
            for transacao in self._historico.transacoes:
                print(f"[{transacao['data']}] {transacao['tipo']}: R$ {transacao['valor']:.2f}")

        print("-----------------------------------------")
        print(f"Saldo: R$ {self._saldo:.2f}")
        print("=========================================")

# ==========================
# CLASSES CONCRETAS
# ==========================
class Usuario(Pessoa):
    """Herda pessoa e representa um usuário do sistema bancário."""
    pass

class ContaCorrente(Conta):
    """Classe concreta que representa uma conta corrente."""
    limite_saque = 500
    max_saques_diarios = 3

    def __init__(self, usuario, senha_4_digitos):
        """Inicializa uma conta corrente."""
        super().__init__(usuario, senha_4_digitos)
        self._numero_saques = 0

class Historico:
    """Classe para armazenar o histórico de transações de uma conta."""
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao): 
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )

class Transacao(ABC):
    """Classe abstrata para representar uma transação bancária."""
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        
        """
        Método abstrato para registrar a transação em uma conta.
        
        Deve ser implementado por todas as subclasses, garantindo que cada tipo 
        de transação tenha um comportamento específico.
        """

        pass # Implementação obrigatória nas subclasses

class Deposito(Transacao):
    """Classe concreta de depósito."""
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        """Registra um depósito na conta."""
        if self._valor > 0:
            conta._saldo += self._valor
            conta._historico.adicionar_transacao(self)
            print(f"\nDepósito de R$ {self._valor:.2f} realizado com sucesso!")
        else:
            print("\nErro: O valor do depósito deve ser positivo.")

class Saque(Transacao):
    """Classe concreta de saque."""
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        """Realiza a operação de saque contendo suas devidas validações e requisitos."""
        if self._valor <= 0:
            print("\nErro: O valor do saque deve ser positivo.")
        elif self._valor > conta.saldo:
            print("\nErro: Saldo insuficiente.")
        elif self._valor > conta.limite_saque:
            print(f"\nErro: O valor do saque excede o limite de R$ {conta.limite_saque}.")
        elif conta._numero_saques >= conta.max_saques_diarios:
            print("\nErro: Número máximo de saques diários excedido.")
        else:
            conta._saldo -= self._valor
            conta._numero_saques += 1
            conta._historico.adicionar_transacao(self)
            print(f"\nSaque de R$ {self._valor:.2f} realizado com sucesso!")


# ==========================
# CLASSE BANCO
# ==========================
class Banco:
    """Classe que representa o banco, gerenciando usuários e contas."""

    def __init__(self):
        """Inicializa o banco com listas vazias de usuários e contas."""
        
        self.usuarios = []
        self.contas = []

    def criar_usuario(self):
        """Solicita os dados do usuário, valida as informações e adiciona um novo usuário ao banco."""
        
        print("\n=== Cadastro de Novo Usuário ===")

        # Coleta e valida o nome do usuário
        while True:
            nome = input("Nome completo: ")
            if validar_nome(nome):
                break
            print("\nErro: Nome inválido! Digite apenas letras.")

        # Coleta e valida a data de nascimento
        while True:
            data_nascimento = input("Data de nascimento (DD/MM/AAAA): ")
            if validar_data_nascimento(data_nascimento):
                break
            print("\nErro: Data de nascimento inválida ou usuário menor de 18 anos.")

        # Coleta e valida o CPF, garantindo que não esteja duplicado
        while True:
            cpf = input("CPF (somente números): ")
            if validar_cpf(cpf) and not any(usuario.cpf == cpf for usuario in self.usuarios):
                break
            print("\nErro: CPF inválido ou já cadastrado!")

        # Coleta e valida o endereço do usuário
        while True:
            endereco = input("Endereço (Logradouro, Número - Bairro - Cidade/UF): ")
            if validar_endereco(endereco):
                break
            print("\nErro: Endereço inválido! Use o formato correto: Rua Exemplo, 123 - Centro - Cidade/UF")

        # Cria um novo usuário e adiciona à lista
        novo_usuario = Usuario(nome, cpf, data_nascimento, endereco)
        self.usuarios.append(novo_usuario)
        print("\nUsuário cadastrado com sucesso!")

    def criar_conta(self):
        """Cria uma nova conta para um usuário existente no banco."""
        
        print("\n=== Cadastro de Nova Conta Corrente ===")

        # Solicita o CPF para encontrar o usuário correspondente
        cpf = input("Informe o CPF do titular da conta: ")
        usuario = next((u for u in self.usuarios if u.cpf == cpf), None)
        if not usuario:
            print("\nErro: Usuário não encontrado!")
            return

        # Solicita e valida a senha da conta
        senha = input("Crie uma senha de 4 dígitos: ")
        while not validar_senha(senha, tamanho=4):
            print("\nErro: A senha deve conter exatamente 4 dígitos numéricos!")
            senha = input("Crie uma senha de 4 dígitos: ")

        # Cria uma conta corrente associada ao usuário
        conta = ContaCorrente(usuario, senha)
        self.contas.append(conta)
        print(f"\nConta criada com sucesso! Agência: {conta.agencia}, Conta: {conta.numero_conta}")

    def acessar_conta(self):
        """Permite ao usuário acessar sua conta bancária informando CPF, agência, número da conta e senha."""
        
        print("\n=== Acesso ao Sistema Bancário ===")

        # Solicita o CPF do usuário
        cpf = input("Informe seu CPF: ")
        contas_usuario = [c for c in self.contas if c._usuario.cpf == cpf]

        # Verifica se há contas associadas ao CPF
        if not contas_usuario:
            print("\nErro: Nenhuma conta cadastrada para este titular.")
            return None

        # Exibe as contas disponíveis para o usuário
        print("\nContas encontradas:")
        for conta in contas_usuario:
            print(f"Agência: {conta.agencia} | Conta: {conta.numero_conta}")

        # Solicita os dados da conta para acesso
        agencia = input("Informe a Agência: ")
        numero_conta = int(input("Informe o Número da Conta: "))

        # Busca a conta informada pelo usuário
        conta = next((c for c in contas_usuario if c.agencia == agencia and c.numero_conta == numero_conta), None)
        if not conta:
            print("\nErro: Conta não encontrada!")
            return None

        # Valida a senha do usuário com limite de tentativas
        tentativas = 3
        while tentativas > 0:
            senha = input("Informe sua Senha de 4 dígitos: ")
            if conta.validar_senha(senha):
                return conta
            else:
                tentativas -= 1
                print(f"\nErro: Senha incorreta! Tentativas restantes: {tentativas}")

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
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            banco.criar_usuario()
        elif opcao == "2":
            banco.criar_conta()
        elif opcao == "3":
            conta = banco.acessar_conta()
            if conta:
                while True:
                    menu_operacoes()
                    opcao_conta = input("Escolha uma opção: ")
                    
                    if opcao_conta == "1":
                        while True:
                            try:
                                valor = float(input("\nValor do depósito: "))
                                if valor > 0:
                                    break
                                else:
                                    print("Erro: O valor do depósito deve ser positivo!")
                            except ValueError:
                                print("Erro: Digite um valor numérico válido!")
                                
                        transacao = Deposito(valor)
                        conta.realizar_transacao(transacao)
                    elif opcao_conta == "2":
                        while True:
                            try:
                                valor = float(input("\nValor do saque: "))
                                if valor > 0:
                                    break
                                else:
                                    print("Erro: O valor do saque deve ser positivo!")
                            except ValueError:
                                print("Erro: Digite um valor numérico válido!")
                                
                        transacao = Saque(valor)
                        conta.realizar_transacao(transacao)
                    elif opcao_conta == "3":
                        conta.exibir_extrato()
                    elif opcao_conta == "4":
                        break
                    else:
                        print("\nOpção inválida!")
        elif opcao == "4":
            break
        else:
            print("\nOpção inválida!")

if __name__ == "__main__":
    main()