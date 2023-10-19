from model.pacientes import Paciente
from model.profissionais import Profissional

class Profissional_responsavel:
    def __init__(self, 
                 cod_relacionamento: int = None,
                 cpf: Paciente = None,
                 contato_envio: Profissional = None
                 ):
        self.set_cod_relacionamento(cod_relacionamento)
        self.set_paciente(cpf)
        self.set_profissional(contato_envio)

    def set_cod_relacionamento(self, cod_relacionamento: int):
        self.cod_relacionamento = cod_relacionamento

    def set_paciente(self, paciente: Paciente):
        self.paciente = paciente

    def set_profissional(self, contato_envio: Profissional):
        self.contato_envio = contato_envio

    def get_cod_relacionamento(self) -> int:
        return self.cod_relacionamento

    def get_paciente(self) -> Paciente:
        return self.paciente

    def get_profissional(self) -> Profissional:
        return self.contato_envio

    def to_string(self) -> str:
        return f"Codigo Relacionamento: {self.get_cod_relacionamento()} | Paciente: {self.get_paciente().get_cpf()} | Profissional: {self.get_profissional().get_nome()}"
