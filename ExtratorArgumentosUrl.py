class ExtratorArgumentoUrl:
    def __init__(self, url):
        if self.Url_valida(url):
            self.url = url.lower()
        else:
            raise LookupError('Url inválida!!!')

    def __len__(self):
        return len(self.url)

    def __str__(self):
        moeda_origem, moeda_destino = self.Extrai_argumentos_find()
        representacao_string = f'Valor: R${self.Extrai_valor()} ' \
                               f'\nMoeda origem: {moeda_origem} ' \
                               f'\nMoeda destino: {moeda_destino}'
        return representacao_string

    def __eq__(self, outro_valor):
        return self.url == outro_valor.url

    @property
    def get_url(self):
        return self.url

    # Verifica se o valor de entrada é != None ou vazio ""
    # e também verifica se a entrada começa com uma string específica 'http..'
    @staticmethod
    def Url_valida(url):
        if url and url.startswith('http://www.byte.com.br/'):
            return True
        else:
            return False

    def Extrai_argumentos_find(self):

        indice_inicial_moeda_origem = self.url.find('=')
        indice_final_moeda_origem = self.url.find('&')

        indice_inicial_moeda_destino = self.url.find('=', 45)
        indice_final_moeda_destino = self.url.find('&', 50)

        moeda_origem = self.url[indice_inicial_moeda_origem + 1: indice_final_moeda_origem]
        moeda_destino = self.url[indice_inicial_moeda_destino + 1: indice_final_moeda_destino]

        return moeda_origem, moeda_destino

    def Extrai_argumentos_len(self):

        moeda_origem_busca = 'moedaorigem='.lower()
        moeda_destino_busca = 'moedadestino='.lower()

        indice_inicial_moeda_origem = self.Encontra_indice_inicial(moeda_origem_busca)
        indice_final_moeda_origem = self.url.find('&')

        moeda_origem = self.url[indice_inicial_moeda_origem : indice_final_moeda_origem]

        if moeda_origem != 'real':
            self.Troca_moeda_origem(moeda_origem)

            indice_inicial_moeda_origem = self.Encontra_indice_inicial(moeda_origem_busca)
            indice_final_moeda_origem = self.url.find('&')
            moeda_origem = self.url[indice_inicial_moeda_origem: indice_final_moeda_origem]

        indice_inicial_moeda_destino = self.Encontra_indice_inicial(moeda_destino_busca)
        indice_final_moeda_destino = self.url.find('&', 50)

        moeda_destino = self.url[indice_inicial_moeda_destino : indice_final_moeda_destino]

        return moeda_origem, moeda_destino

    def Encontra_indice_inicial(self,moeda):
        return self.url.find(moeda) + len(moeda)

    def Troca_moeda_origem(self, erro):
        self.url = self.url.replace(erro, 'real', 1)

    def Extrai_valor(self):
        busca_valor = 'valor='
        indice_inicial_valor = self.Encontra_indice_inicial(busca_valor)
        valor = self.url[indice_inicial_valor:]
        return valor
