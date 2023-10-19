class Paciente:
    def __init__(self,
                 CPF: str = None, 
                 nome_paciente: str = None,
                 idade: int = None,
                 tamanho_abdominal: float = None,
                 altura_cm: float = None,
                 peso_kg: float = None,
                ):
        self.set_CPF(CPF)
        self.set_nome_paciente(nome_paciente)
        self.set_idade(idade)
        self.set_tamanho_abdominal(tamanho_abdominal)
        self.set_altura_cm(altura_cm)
        self.set_peso_kg(peso_kg)
    
    def set_CPF(self, CPF: str):
        self.CPF = CPF

    def set_nome_paciente(self, nome_paciente: str):
        self.nome_paciente = nome_paciente

    def set_idade(self, idade: int):
        self.idade = idade 

    def set_tamanho_abdominal(self, tamanho_abdominal: float):
        self.tamanho_abdominal = tamanho_abdominal

    def set_altura_cm(self, altura_cm: float):
        self.altura_cm = altura_cm

    def set_peso_kg(self, peso_kg: float):
        self.peso_kg = peso_kg

    def set_peso_objetivo(self, peso_objetivo: float):
        self.peso_objetivo = peso_objetivo

    def get_CPF(self) -> str:
        return self.CPF

    def get_nome_paciente(self) -> str:
        return self.nome_paciente

    def get_idade(self) -> int:
        return self.idade

    def get_tamanho_abdominal(self) -> float:
        return self.tamanho_abdominal

    def get_altura_cm(self) -> float:
        return self.altura_cm

    def get_peso_kg(self) -> float:
        return self.peso_kg

    def get_peso_objetivo(self) -> float:
        return self.peso_objetivo

    def to_string(self) -> str:
        return f"CPF: {self.get_CPF()} | Nome: {self.get_nome_paciente()} | Idade: {self.get_idade()} | Tamanho Abdominal: {self.get_tamanho_abdominal()} | Altura: {self.get_altura_cm()} | Peso: {self.get_peso_kg()} | Peso Objetivo: {self.get_peso_objetivo()}"