class Pessoa:
    def __init__(self, *filhos, nome=None, idade=25):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def comprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    Giovanni = Pessoa(nome='Giovanni')
    Ademir = Pessoa(Giovanni, nome='Ademir')
    print(Pessoa.comprimentar(Ademir))
    print(id(Ademir))
    print(Ademir.comprimentar())
    print(Ademir.nome)
    print(Ademir.idade)
    for filho in Ademir.filhos:
        print(filho.nome)
