class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def adicao(self):
        return self.num1 + self.num2

    def subtracao(self):
        return self.num1 - self.num2

    def multiplicacao(self):
        return self.num1 * self.num2

    def divisao(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Erro: Divisão por zero não é permitida."

calculadora = Calculadora(10, 5)

print("Adição:", calculadora.adicao())
print("Subtração:", calculadora.subtracao())
print("Multiplicação:", calculadora.multiplicacao())
print("Divisão:", calculadora.divisao())

calculadora = Calculadora(20, 0)
print("Divisão por zero:", calculadora.divisao())