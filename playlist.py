class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    def dar_like(self):
        self._likes +=1

    def __str__(self):
        return f'{self._nome} - {self.ano} : {self._likes} Likes.'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome,ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome} - Ano {self.ano} - {self.duracao} Min: {self._likes} Likes.'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - Ano {self.ano} - {self.temporadas} Temporadas: {self._likes} Likes.'

class Playlist:
    def __init__(self,nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)

#------------------------------ Fim do Programa ------------------------------

# cadastro de programas (Filmes e Series)
vingadores = Filme('vingadores; guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('Todo mundo em panico', 1999, 100)
demolidor = Serie('demolidor', 2016, 2)

# teste dar_like() para os programas
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
tmep.dar_like()
tmep.dar_like()
demolidor.dar_like()
atlanta.dar_like()
atlanta.dar_like()

# cria lista com os programas cadastrados
filmes_e_series = [vingadores, atlanta, demolidor, tmep]

# cria playlist que contem a lista de programas cadastrados
playlist_fim_de_semana = Playlist('Fim de semana', filmes_e_series)

# iteração da playlist
for programa in playlist_fim_de_semana:
    print(programa)

print(f'Tamanho da playlist {playlist_fim_de_semana.nome}: {len(playlist_fim_de_semana)} programas.')

print(f'Demolidor está na playlist_fim_de_semana? {demolidor in playlist_fim_de_semana}')

print(playlist_fim_de_semana[1])