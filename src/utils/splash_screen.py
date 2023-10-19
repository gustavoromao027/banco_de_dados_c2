from conexion.oracle_queries import OracleQueries
from utils import config

class SplashScreen:

    def __init__(self):
        # Consultas de contagem de registros - inicio
        self.qry_total_pacientes = config.QUERY_COUNT.format(tabela="pacientes")
        self.qry_total_profissionais = config.QUERY_COUNT.format(tabela="profissionais")
        # Consultas de contagem de registros - fim

        # Nome(s) do(s) criador(es)
        self.created_by = """Ana Karla Vianna Tacon, Gustavo Romão Cunha, Glabson Firmino da Silva Junior, Juliana Torres Deluarno, Igor Nunes Carolino, Ramon Oliveira Nascimento, Wendell Athaides Grippa"""
        self.professor = "Prof. M.Sc. Howard Roatti"
        self.disciplina = "Banco de Dados"
        self.semestre = "2023/2"

    def get_total_pacientes(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Retorna o total de registros computado pela query
        return oracle.sqlToDataFrame(self.qry_total_pacientes)["total_pacientes"].values[0]

    def get_total_profissionais(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Retorna o total de registros computado pela query
        return oracle.sqlToDataFrame(self.qry_total_profissionais)["total_clientes"].values[0]


    def get_updated_screen(self):
        return f"""
        ########################################################
        #                   SISTEMA DE MEDIÇÃO                     
        #                                                         
        #  TOTAL DE REGISTROS:                                    
        #      1 - PACIENTES:         {str(self.get_total_pacientes()).rjust(5)}
        #      2 - PROFISSIONAIS:         {str(self.get_total_profissionais()).rjust(5)}
        #
        #  CRIADO POR: {self.created_by}
        #
        #  PROFESSOR:  {self.professor}
        #
        #  DISCIPLINA: {self.disciplina}
        #              {self.semestre}
        ########################################################
        """