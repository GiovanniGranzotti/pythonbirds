class Pessoa:
    def comprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    P = Pessoa()
    print(Pessoa.comprimentar(P))
    print(id(P))
    print(P.comprimentar())