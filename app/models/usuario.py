class Usuario:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

    def autenticar(self, senha_digitada):
        return self.senha == senha_digitada
