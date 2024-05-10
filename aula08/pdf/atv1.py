class Cachorro:
    def __init__(self,nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade

    def latir(self): 
        return f"E o {self.nome} está latindo"
    def dados(self):
        return f"O {self.nome} tem {self.idade} anos e é da raça {self.raca}"
    
cachorrinho = Cachorro("max", "york", 19)

print(cachorrinho.dados())
print(cachorrinho.latir())

