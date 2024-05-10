class Empresa:
    def __init__(self,nome,cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def dados(self): 
        return f"Nome: {self.nome}, Cargo: {self.cargo}, Salario: {self.salario} Reais"

    
pessoa1 = Empresa("Max","Programador",2000)
pessoa2 = Empresa("Maria","Gerente",3000)

print(pessoa1.dados())
print(pessoa2.dados())