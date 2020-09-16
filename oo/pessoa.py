class Pessoa:
    def __init__(self, nome=None, idade=25):
        self.idade = idade
        self.nome = nome

    def comprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    P = Pessoa('Luciano')
    print(Pessoa.comprimentar(P))
    print(id(P))
    print(P.comprimentar())
    print(P.nome)
    P.nome = 'Giovanni'
    print(P.nome)
    print(P.idede)
