# Classe base Pessoa
class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self._cpf = cpf  # Atributo sensível encapsulado

    def mostrar_info(self):
        print(f'Nome: {self.nome}, Idade: {self.idade}')


# Classe Paciente (herança de Pessoa)
class Paciente(Pessoa):
    def __init__(self, nome, idade, cpf, historico):
        super().__init__(nome, idade, cpf)
        self._historico = historico  # Encapsulando atributo sensível

    def mostrar_info(self):
        super().mostrar_info()
        print(f'Histórico: {self._historico}')


# Classe Médico (herança de Pessoa)
class Medico(Pessoa):
    def __init__(self, nome, idade, cpf, especialidade):
        super().__init__(nome, idade, cpf)
        self.especialidade = especialidade

    def mostrar_info(self):
        super().mostrar_info()
        print(f'Especialidade: {self.especialidade}')


# Classe Consulta
class Consulta:
    def __init__(self, paciente, medico, data):
        self.paciente = paciente
        self.medico = medico
        self.data = data

    def mostrar_info(self):
        print(f'Consulta marcada para {self.data}')
        print(f'Paciente: {self.paciente.nome}')
        print(f'Médico: {self.medico.nome} - {self.medico.especialidade}')


# Testando o código
# Criando instâncias de Paciente e Médico
paciente1 = Paciente("João Silva", 30, "123.456.789-00", "Histórico: Alergias a medicamentos")
medico1 = Medico("Dra. Ana", 45, "987.654.321-00", "Cardiologia")

# Criando uma consulta
consulta1 = Consulta(paciente1, medico1, "20/11/2024")

# Mostrando informações
print("Informações do Paciente:")
paciente1.mostrar_info()
print("\nInformações do Médico:")
medico1.mostrar_info()
print("\nInformações da Consulta:")
consulta1.mostrar_info()
