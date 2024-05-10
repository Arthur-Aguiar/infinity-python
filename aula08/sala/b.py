class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = 0  # Inicializar o atributo velocidade com zero
    
    def acelerar(self):
        self.velocidade += 10
        print(f"{self.marca} {self.modelo} acelerando. Velocidade atual: {self.velocidade} km/h")
    
    def frear(self):
        self.velocidade -= 5
        print(f"{self.marca} {self.modelo} freando. Velocidade atual: {self.velocidade} km/h")

# Criando um objeto da classe Carro
meu_carro = Carro("Ford", "Mustang")

# Utilizando a abstração para interagir com o carro
meu_carro.acelerar()
meu_carro.frear()
