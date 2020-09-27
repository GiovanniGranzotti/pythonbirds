class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=25):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def comprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 43

    @classmethod
    def nome_e_atributo_de_classe(cls):
        return f'{cls} - olhos: {cls.olhos}'


class Homem(Pessoa):
    pass


if __name__ == '__main__':
    Giovanni = Homem(nome='Giovanni')
    Ademir = Homem(Giovanni, nome='Ademir')
    print(Pessoa.comprimentar(Ademir))
    print(id(Ademir))
    print(Ademir.comprimentar())
    print(Ademir.nome)
    print(Ademir.idade)
    for filho in Ademir.filhos:
        print(filho.nome)
    Ademir.sobrenome = 'Granzotti'
    del Ademir.filhos
    Ademir.olhos = 1
    del Ademir.olhos
    print(Ademir.__dict__)
    print(Giovanni.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(Giovanni.olhos)
    print(Ademir.olhos)
    print(id(Pessoa.olhos), id(Giovanni.olhos), id(Ademir.olhos))
    print(Pessoa.metodo_estatico(), Ademir.metodo_estatico())
    print(Pessoa.nome_e_atributo_de_classe(), Ademir.nome_e_atributo_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(Giovanni, Pessoa))
    print(isinstance(Giovanni, Homem))
