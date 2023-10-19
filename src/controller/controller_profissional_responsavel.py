from model.pacientes import Paciente
from model.profissionais import Profissional
from model.profissionais_responsaveis import Profissional_responsavel

from controller.controller_paciente import Controller_Paciente
from controller.controller_profissional import Controller_Profissional

from conexion.oracle_queries import OracleQueries

class Controller_Profissional_Responsavel:
    def __init__(self):
        self.ctrl_paciente = Controller_Paciente()
        self.ctrl_profissional = Controller_Profissional()
        self.cod_relacionamento = 0  # Inicializa o contador de relacionamentos

    def obter_proximo_cod_relacionamento(self):
        self.cod_relacionamento += 1
        return self.cod_relacionamento

    def inserir_profissionais_responsaveis(self) -> Profissional_responsavel:
        oracle = OracleQueries()

        self.listar_pacientes(oracle, need_connect=True)
        cpf = str(input("Digite o número do CPF do Paciente: "))
        paciente = self.valida_paciente(oracle, cpf)
        if paciente is None:
            return None

        self.listar_profissionais(oracle, need_connect=True)
        licenca = str(input("Digite a Licença do Profissional: "))
        profissional = self.valida_profissional(oracle, licenca)
        if profissional is None:
            return None

        cursor = oracle.connect()
        output_value = cursor.var(int)

        data = dict(
            cod_relacionamento=self.obter_proximo_cod_relacionamento(),
            cpf=paciente.get_CPF(),
            licenca=profissional.get_Licenca()
        )

        cursor.execute("""
        begin
            :codigo := :codigo + 1;
            insert into profissionais_responsaveis values(:cod_relacionamento, :, :cpf, :licenca);
        end;
        """, data)

        cod_relacionamento = output_value.getvalue()
        oracle.conn.commit()
        bd_profissionais_responsaveis = oracle.sqlToDataFrame(f"select cod_relacionamento, cpf, licenca from profissionais_responsaveis where cod_relacionamento = {cod_relacionamento}")
        novo_profissional_responsavel = cod_relacionamento(bd_profissionais_responsaveis.cod_relacionamento.values[0], bd_profissionais_responsaveis.cpf.values[0], paciente, profissional)
        print(novo_profissional_responsavel.to_string())
        return novo_profissional_responsavel
    
    def atualizar_profissional_responsavel(self) -> Profissional_responsavel:
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o código do produto a ser alterado
        cod_relacionamento = int(input("Código do Relacionamento que irá alterar: "))        

        # Verifica se o produto existe na base de dados
        if not self.verifica_existencia_profissionais_responsaveis(oracle, cod_relacionamento):

            # Lista os pacientes existentes para inserir no Relacionamento
            self.listar_pacientes(oracle)
            cpf = str(input("Digite o número do CPF do Paciente: "))
            paciente = self.valida_paciente(oracle, cpf)
            if paciente == None:
                return None

            # Lista os profissionais existentes para inserir no Relacionamento
            self.listar_profissionais(oracle)
            licenca = str(input("Digite o número da Licença do Profissional: "))
            profissional = self.valida_profissional(oracle, licenca)
            if profissional == None:
                return None

            # Atualiza a descrição do produto existente
            oracle.write(f"update profissionais_responsaveis set cpf = '{paciente.get_CPF()}', licenca = '{profissional.get_licenca()}', where cod_relacionamento = {cod_relacionamento}")
            # Recupera os dados do novo produto criado transformando em um DataFrame
            bd_profissionais_responsaveis = oracle.sqlToDataFrame(f"select cod_relacionamento, cpf, licenca from profissionais_responsaveis where cod_relacionamento = {cod_relacionamento}")
            # Cria um novo objeto Produto
            profissionais_responsaveis_atualizados = cod_relacionamento(bd_profissionais_responsaveis.codigo_agendamento.values[0], bd_profissionais_responsaveis.data_agendamento.values[0], paciente, profissional)
            # Exibe os atributos do novo produto
            print(profissionais_responsaveis_atualizados.to_string())
            # Retorna o objeto agendamento_atualizado para utilização posterior, caso necessário
            return profissionais_responsaveis_atualizados
        else:
            print(f"O código {cod_relacionamento} não existe.")
            return None
        
    def excluir_profissionais_responsaveis(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o código do produto a ser alterado
        cod_relacionamento = int(input("Código do Agendamento que irá excluir: "))        

        # Verifica se o produto existe na base de dados
        if not self.verifica_existencia_profissionais_reponsaveis(oracle, cod_relacionamento):            
            # Recupera os dados do novo produto criado transformando em um DataFrame
            bd_profissionais_responsaveis = oracle.sqlToDataFrame(f"select cod_relacionamento, cpf, licenca from agendamentos where cod_relacionamento = {cod_relacionamento}")
            paciente = self.valida_paciente(oracle, bd_profissionais_responsaveis.cpf.values[0])
            profissional = self.valida_profissional(oracle, bd_profissionais_responsaveis.licenca.values[0])
            
            opcao_excluir = input(f"Tem certeza que deseja excluir o agendamento {cod_relacionamento} [S ou N]: ")
            if opcao_excluir.lower() == "s":
                print("Atenção, caso o paciente possua profissionais, também serão excluídos!")
                # Revome o profissional da tabela
                oracle.write(f"delete from agendamentos where codigo_agendamento = {cod_relacionamento}")
                # Cria um novo objeto Produto para informar que foi removido
                profissionais_responsaveis_excluido = cod_relacionamento(bd_profissionais_responsaveis.codigo_agendamento.values[0], bd_profissionais_responsaveis.data_agendamento.values[0], paciente, profissional)
                # Exibe os atributos do produto excluído
                print("Agendamento Removido com Sucesso!")
                print(profissionais_responsaveis_excluido.to_string())
        else:
            print(f"O código {cod_relacionamento} não existe.")

    def verifica_existencia_profissionais_reponsaveis(self, oracle:OracleQueries, cod_relacionamento:int=None) -> bool:
        # Recupera os dados do novo agendamento criado transformando em um DataFrame
        bd_profissionais_responsaveis = oracle.sqlToDataFrame(f"select cod_relacionamento, cpf, licenca from agendamentos where cod_relacionamento = {cod_relacionamento}")
        return bd_profissionais_responsaveis.empty

    def listar_pacientes(self, oracle:OracleQueries, need_connect:bool=False):
        query = """
                select c.cpf
                    , c.nome 
                from pacientes c
                order by c.nome
                """
        if need_connect:
            oracle.connect()
        print(oracle.sqlToDataFrame(query))

    def listar_profissionais(self, oracle:OracleQueries, need_connect:bool=False):
        query = """
                select f.licenca
                    , f.nome
                from profissionais f
                order by f.nome
                """
        if need_connect:
            oracle.connect()
        print(oracle.sqlToDataFrame(query))

    def valida_paciente(self, oracle:OracleQueries, cpf:str=None) -> Paciente:
        if self.ctrl_paciente.verifica_existencia_paciente(oracle, cpf):
            print(f"O CPF {cpf} informado não existe na base.")
            return None
        else:
            oracle.connect()
            # Recupera os dados do novo paciente criado transformando em um DataFrame
            bd_paciente = oracle.sqlToDataFrame(f"select cpf, nome from pacientes where cpf = {cpf}")
            # Cria um novo objeto paciente
            paciente = Paciente(bd_paciente.cpf.values[0], bd_paciente.nome.values[0])
            return paciente

    def valida_profissional(self, oracle:OracleQueries, licenca:str=None) -> Profissional:
        if self.ctrl_profissional.verifica_existencia_profissionais_responsaveis(oracle, licenca):
            print(f"A licenca {licenca} informada não existe na base.")
            return None
        else:
            oracle.connect()
            # Recupera os dados do novo Profissional criado transformando em um DataFrame
            bd_profissionais = oracle.sqlToDataFrame(f"select licenca, nome from profissionais where licenca = {licenca}")
            # Cria um novo objeto Profissional
            profissionais = Profissional(bd_profissionais.licenca.values[0], bd_profissionais.nome.values[0])
            return profissionais