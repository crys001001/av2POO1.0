# class Pessoa:
#     def _init_(self, nome, idade, cpf, endereco):
#         self.nome = nome
#         self.idade = idade
#         self._cpf = cpf  # Encapsulamento
#         self.endereco = endereco

#     def mostrar_informacoes(self):
#         print(f'Nome: {self.nome}, Idade: {self.idade}, CPF: {
#               self._cpf}, Endereço: {self.endereco}')


# class Paciente(Pessoa):
#     def _init_(self, nome, idade, cpf, endereco, historico):
#         # Aqui chamei o construtor da classe Pessoa
#         super()._init_(nome, idade, cpf, endereco)
#         self.historico = historico
#         self.prontuarios = []  # Criei uma lista para armazenar os prontuários

#     def mostrar_informacoes(self):
#         super().mostrar_informacoes()
#         print(f'Histórico: {self.historico}')
#         self.listar_prontuarios()  # Mostra os prontuários diretamente nas informações

#     def adicionar_prontuario(self, prontuario):
#         self.prontuarios.append(prontuario)
#         print(f"Prontuário adicionado para o paciente: {self.nome}")

#     def listar_prontuarios(self):
#         if self.prontuarios:
#             print("Prontuários:")
#             for prontuario in self.prontuarios:
#                 # Aqui o método _str_ da classe Prontuario será usado
#                 print(prontuario)
#         else:
#             print("Nenhum prontuário registrado.")


# class Medico(Pessoa):
#     def _init_(self, nome, idade, cpf, endereco, especialidade):
#         super()._init_(nome, idade, cpf, endereco)
#         self.especialidade = especialidade

#     def mostrar_informacoes(self):
#         super().mostrar_informacoes()
#         print(f'Especialidade: {self.especialidade}')


# class Consulta:
#     def _init_(self, paciente, medico, data_consulta):
#         self.paciente = paciente
#         self.medico = medico
#         self.data_consulta = data_consulta

#     def mostrar_consulta(self):
#         print(f'Paciente: {self.paciente.nome}, Médico: {
#               self.medico.nome}, Data: {self.data_consulta}')


# class Prontuario:
#     def _init_(self, paciente, diagnostico, observacao):
#         self.paciente = paciente
#         self._diagnostico = diagnostico  # Encapsulamento
#         self.observacao = observacao

#     def adicionar_observacao(self, observacao):
#         self.observacao = observacao

#     def _str_(self):
#         return f'Paciente: {self.paciente.nome}, Diagnóstico: {self._diagnostico}, Observação: {self.observacao}'

#     # Testando o sistema
# if _name_ == "_main_":
#     # Criando um paciente
#     paciente1 = Paciente("João", 30, "123456789",
#                          "Rua A, nº 10", "Sem histórico")

#     # Criando um médico
#     medico1 = Medico("Dra. Ana", 40, "987654321",
#                      "Avenida B, nº 20", "Cardiologia")

#     # Criando uma consulta
#     consulta1 = Consulta(paciente1, medico1, "20/11/2024")

#     # Criando um prontuário
#     prontuario1 = Prontuario(paciente1, "Hipertensão", "Acompanhamento mensal")

#     # Adicionando o prontuário ao paciente
#     paciente1.adicionar_prontuario(prontuario1)

#     # Mostrando informações
#     print("\n--- Informações do Paciente ---")
#     paciente1.mostrar_informacoes()

#     print("\n--- Informações da Consulta ---")
#     consulta1.mostrar_consulta()

#     print("\n--- Informações do Prontuário ---")
#     paciente1.listar_prontuarios()


class Pessoa:
    def _init_(self, nome, idade, cpf, endereco):
        self.nome = nome
        self.idade = idade
        self._cpf = cpf  # Encapsulamento
        self.endereco = endereco

    def mostrar_informacoes(self):
        print(self)

    def _str_(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, CPF: {self._cpf}, Endereço: {self.endereco}"


class Paciente(Pessoa):
    def _init_(self, nome, idade, cpf, endereco, historico):
        # Chamando o construtor da classe Pessoa
        super()._init_(nome, idade, cpf, endereco)
        self._historico = historico  # Encapsulamento do histórico
        self.prontuarios = []  # Lista para armazenar os prontuários

    def mostrar_informacoes(self):
        super().mostrar_informacoes()
        print(f"Histórico: {self._historico}")
        self.listar_prontuarios()  # Mostra os prontuários diretamente nas informações

    def adicionar_prontuario(self, prontuario):
        self.prontuarios.append(prontuario)
        print(f"Prontuário adicionado para o paciente: {self.nome}")

    def listar_prontuarios(self):
        if self.prontuarios:
            print("Prontuários:")
            for prontuario in self.prontuarios:
                print(prontuario)  # Usa o _str_ da classe Prontuario
        else:
            print("Nenhum prontuário registrado.")

    def _str_(self):
        return super()._str_() + f", Histórico: {self._historico}"


class Medico(Pessoa):
    def _init_(self, nome, idade, cpf, endereco, especialidade):
        super()._init_(nome, idade, cpf, endereco)
        self.especialidade = especialidade

    def mostrar_informacoes(self):
        super().mostrar_informacoes()
        print(f"Especialidade: {self.especialidade}")

    def _str_(self):
        return super()._str_() + f", Especialidade: {self.especialidade}"


class Consulta:
    def _init_(self, paciente, medico, data_consulta):
        self.paciente = paciente
        self.medico = medico
        self.data_consulta = data_consulta

    def mostrar_consulta(self):
        print(self)

    def _str_(self):
        return f"Paciente: {self.paciente.nome}, Médico: {self.medico.nome}, Data: {self.data_consulta}"


class Prontuario:
    def _init_(self, paciente, diagnostico, observacao):
        self.paciente = paciente
        self._diagnostico = diagnostico  # Encapsulamento
        self.observacao = observacao

    def adicionar_observacao(self, observacao):
        self.observacao = observacao

    def _str_(self):
        return f"Paciente: {self.paciente.nome}, Diagnóstico: {self._diagnostico}, Observação: {self.observacao}"


# Função para cadastrar pacientes
def cadastrar_paciente():
    nome = input("Digite o nome do paciente: ")
    idade = int(input("Digite a idade do paciente: "))
    cpf = input("Digite o CPF do paciente: ")
    endereco = input("Digite o endereço do paciente: ")
    historico = input("Digite o histórico do paciente: ")
    return Paciente(nome, idade, cpf, endereco, historico)


# Função para cadastrar médicos
def cadastrar_medico():
    nome = input("Digite o nome do médico: ")
    idade = int(input("Digite a idade do médico: "))
    cpf = input("Digite o CPF do médico: ")
    endereco = input("Digite o endereço do médico: ")
    especialidade = input("Digite a especialidade do médico: ")
    return Medico(nome, idade, cpf, endereco, especialidade)


# Testando o sistema
if __name__ == "__main__":
    # Listas para armazenar os dados
    pacientes = []
    medicos = []
    consultas = []

    # Cadastrando um paciente
    paciente1 = cadastrar_paciente()
    pacientes.append(paciente1)

    # Cadastrando um médico
    medico1 = cadastrar_medico()
    medicos.append(medico1)

    # Criando uma consulta
    consulta1 = Consulta(paciente1, medico1, "20/11/2024")
    consultas.append(consulta1)

    # Criando um prontuário
    prontuario1 = Prontuario(paciente1, "Hipertensão", "Acompanhamento mensal")
    paciente1.adicionar_prontuario(prontuario1)

    # Mostrando informações
    print("\n--- Informações do Paciente ---")
    paciente1.mostrar_informacoes()

    print("\n--- Informações do Médico ---")
    medico1.mostrar_informacoes()

    print("\n--- Informações da Consulta ---")
    consulta1.mostrar_consulta()

    print("\n--- Informações do Prontuário ---")
    paciente1.listar_prontuarios()