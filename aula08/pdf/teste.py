class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def adicionar_funcionario(self, nome, cargo, salario):
        funcionario = {"nome": nome, "cargo": cargo, "salario": salario}
        self.funcionarios.append(funcionario)

    def remover_funcionario(self, nome):
        for funcionario in self.funcionarios:
            if funcionario["nome"] == nome:
                self.funcionarios.remove(funcionario)
                return True
        return False

    def listar_funcionarios(self):
        for funcionario in self.funcionarios:
            print(f"Nome: {funcionario['nome']}, Cargo: {funcionario['cargo']}, Salário: {funcionario['salario']}")

# Exemplo de uso
empresa = Empresa("Acme Inc.")

empresa.adicionar_funcionario("Max", "Programador", 2000)
empresa.adicionar_funcionario("Maria", "Gerente", 3000)

empresa.listar_funcionarios()
print()

empresa.remover_funcionario("Max")

empresa.listar_funcionarios()