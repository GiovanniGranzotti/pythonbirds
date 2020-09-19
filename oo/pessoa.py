class Pessoa:
    olhos = 2

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
