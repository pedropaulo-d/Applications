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
    def nome(self, novo_name):
        self._nome = novo_name.title()

    def curti(self):
        self._likes += 1

    def __str__(self):
        return f'Nome: {self._nome}, Ano: {self.ano}, Likes: {self._likes}'

class Filmes(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self._nome} - Duração: {self.duracao}min - Ano: {self.ano} - Likes: {self._likes}'

class Animes(Programa):
    def __init__(self, nome, ano, episodios):
        super().__init__(nome, ano)
        self.episodios = episodios

    def __str__(self):
        return f'Nome: {self._nome} - Episódios: {self.episodios}eps - Ano: {self.ano} - Likes: {self._likes}'

class Playlist():
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)

classe = Filmes('a voz do silêncio', 2016, 129)
classe2 = Animes('one piece', 1999, 1012)
classe3 = Animes('fairy tail', 2009, 328)
classe4 = Filmes('a viagem de chihiro', 2001, 125)
classe2.curti()
classe2.curti()
classe3.curti()
classe3.curti()
classe4.curti()
classe4.curti()
classe4.curti()
classe2.curti()
classe.curti()
classe.curti()
print('-'*100)

filmes_e_animes = [classe, classe2, classe3, classe4]
minha_list = Playlist('my List', filmes_e_animes)
print(f'Tamanho: {len(minha_list)}')
for programa in minha_list:
    print(programa)
