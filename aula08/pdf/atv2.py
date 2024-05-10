class Pessoa:
    def __init__(self,nome,idade, peso,genero ):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.genero = genero

    def dados(self): 
        return f"Nome: {self.nome}, Idade: {self.idade}, Peso: {self.peso} kg, Gênero: {self.genero}"

    
pessoa1 = Pessoa("Max", 60, 80, "Masculino")
pessoa2 = Pessoa("Maria",15,60, "Feminino")

print(pessoa1.dados())
print(pessoa2.dados())
