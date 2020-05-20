
class Conta:

    def __init__(self, numero, titular, saldo, limite=1000):
        print('contruindo objeto...{}'.format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    # metodo estático: forma de acessar um método antes de definir qualquer objeto
    # acesso: > Conta.codigo_meu_banco()
    @staticmethod
    def codigo_meu_banco():
        return '001'

    # metodo estático > lista com código dos bancos
    @staticmethod
    def codigo_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}

    @titular.setter
    def titular(self, titular):
        self.titular = titular

    @limite.setter
    def limite(self,limite):
        self.__limite = limite

    def extrato(self):
        print(f'Saldo de R${self.__saldo} do cliente titular {self.__titular}.')

    def depositar(self, valor):
        self.__saldo += valor

    # testa se o valor disponível (saldo+limite) é maior que o valor da operação
    def __teste_operacao(self, valor_da_operacao):
        valor_disponivel = self.saldo + self.limite
        return valor_disponivel >= valor_da_operacao

    # se: valor da operação > valor disponivel
    # testa se o cliente deseja realizar a operação com o limite do valor da operação
    def __retorno_indisponivel(self, valor, operacao, destino='molde'):
        valor_disponivel = self.saldo + self.limite
        print(f'O valor de R$ {valor} ultrapassa o saldo disponível em R$ {valor - valor_disponivel}.')
        if valor_disponivel > 0:
            resposta = str(input(f'Deseja {operacao} o total disponível: R$ {valor_disponivel} [s/n]?')).strip().upper()[0]
            if resposta in 'S' and operacao == 'sacar':
                self.sacar(valor_disponivel)
            elif resposta in 'S' and operacao == 'transferir':
                self.transferir(valor_disponivel, destino)
            else:
                print('Operação não concluída!')
        else:
            print(f'Você não possui saldo disponível para {operacao}.')

    def sacar(self, valor):
        if self.__teste_operacao(valor):
            self.__saldo -= valor
        else:
            self.__retorno_indisponivel(valor, 'sacar')

    def transferir(self, valor, destino):
        if self.__teste_operacao(valor):
            self.sacar(valor)
            destino.depositar(valor)
        else:
            self.__retorno_indisponivel(valor, 'transferir', destino)