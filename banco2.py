from abc import ABC, abstractmethod
usuarios = {}
#Menu Sistema Bancário

def inicializar():
    print( 
        
'''=========== Sistema Bancário ===========\n
Digite a opção desejada:
[0] - Sair
[1] - Saque
[2] - Depósito
[3] - Extrato
[4] - Criar Conta
[5] - Criar Usuário

=========================================\n'''.center(50))
    
class Conta:
    def __init__(self,_saldo,_numero,_agencia,_cliente,_historico):
        self._saldo = _saldo
        self._numero = _numero
        self._agencia = _agencia
        self._cliente = _cliente
        if _historico is None:
            self._historico = []
        else:
            self._historico = list(_historico) 
    
    def depositar(self, valor): #valida e atualiza o saldo
        try:
            valor = float(valor)
        except ValueError: 
            return False
        
        if valor <= 0:
            return False
        
        self._saldo += valor
        descricao = f'Depósito: R$ {valor} adicionado ao saldo!'
        self._historico.append(descricao)
        return True

    def sacar(self,valor): #valida saldo, retorna true or false
        try:
            valor = float(valor)
        except ValueError:
            return False
        
        if valor <= 0:
            return False
        
        if valor > self._saldo:
            return False
        
        self._saldo -= valor
        descricao = f'Saque no valor de R${valor} retirado do saldo!'
        self._historico.append(descricao)
        return True

    @property
    def ver_saldo(self): #retorna saldo em float
        return float(self._saldo)

    @classmethod
    def nova_conta(cls, cliente, numero, agencia='0001'): #definir como classmethod
        return cls(0.0, numero, agencia,cliente, None)

class Transacao(ABC):
    def __init__(self, _valor):
        try:
            self._valor = float(_valor)
        except ValueError:
            raise TypeError ('Valor inválido para transação.')
        
    @property
    def valor(self):
        return self._valor

    @abstractmethod
    def registrar(self, conta):
        pass

    def __str__(self):
        return f'{self.__class__.__name__}: R$ {self._valor:.2f}.'
    
class Deposito(Transacao):
    def registrar(self, conta):
        return conta.depositar(self.valor)


class Saque(Transacao):
    def registrar(self, conta):
        return conta.sacar(self.valor)

        
class ContaCorrente(Conta):
    def __init__(self,cliente, numero, saldo_inicial=0.0, agencia='0001', historico=None, limite=500, limite_saques=3):
        super().__init__(saldo_inicial, numero, agencia, cliente, historico,) #super().__init__ serve para puxar os parâmetros da classe Pai
        
        self.limite = float(limite)
        self.limite_saques = int(limite_saques)
        self.saques_realizados = 0

    def sacar(self, valor):
        try:
            valor = float(valor)
        except ValueError:
            return False

        if valor <=0:
            return False
        if valor > self.limite:
            return False
        if self.saques_realizados >= self.limite_saques:
            return False
        if valor > self._saldo:
            return False
        
        resultado = super().sacar(valor)
        if resultado == True:
            self.saques_realizados += 1
            return True
        else: 
            return False


class Cliente:
    def __init__(self, nome, endereco, contas=None):
        self._nome = nome
        self._endereco = endereco
        if contas is None:
            self._contas = []
        else:
            self._contas = list(contas)

    def adicionar_conta(self, conta):
        """Adiciona uma conta ao cliente; retorna True se adicionou, False se já existia."""
        if conta not in self._contas:
            self._contas.append(conta)
            return True
        return False

    def realizar_transacao(self, conta, transacao):
        """Executa transacao apenas se a conta pertence ao cliente."""
        if conta not in self._contas:
            return False
        return transacao.registrar(conta)
    
    @property
    def nome(self):
        return self._nome


class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_nascimento, endereco, contas=None):
        super().__init__(nome, endereco, contas)
        self._cpf = str(cpf)
        self._data_nascimento = data_nascimento

    @property
    def cpf(self):
        return self._cpf



cc = ContaCorrente("João", "1001")
Deposito(200).registrar(cc)
Saque(150).registrar(cc)
print(cc._saldo)
print(cc._numero)
print(cc._agencia)
print(cc._cliente)
print(cc._historico)
print(cc.limite)
print(cc.limite_saques)
print(cc.saques_realizados)
