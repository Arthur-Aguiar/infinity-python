class Carro:
    def __init__(self, marca, modelo, ano, possui_4_rodas):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.possui_4_rodas = possui_4_rodas
    
    def ligar(self): 
        return f"O {self.modelo} está ligado"

orochinho = Carro("Renault", "Oroch", 2019, True)
print(orochinho.modelo)
print(orochinho.ligar())
