from conexion.oracle_queries import OracleQueries

class Relatorio:
    def __init__(self):
        # Abre o arquivo com a consulta e associa a um atributo da classe
        with open("sql/pacientes_com_profissionais.sql") as f:
            self.query_relatorio_pacientes_com_profissionais = f.read()

        # Abre o arquivo com a consulta e associa a um atributo da classe
        with open("sql/relatorio_pacientes.sql") as f:
            self.query_relatorio_pacientes = f.read()

        # Abre o arquivo com a consulta e associa a um atributo da classe
        with open("sql/relatorio_profissionais.sql") as f:
            self.query_relatorio_profissionais = f.read()

    def get_relatorio_pacientes_com_profissionais(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_pacientes_com_profissionais))
        input("Pressione Enter para Sair do Relatório de Pacientes com Profissionais")

    def get_relatorio_pacientes(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_pacientes))
        input("Pressione Enter para Sair do Relatório de Pacientes")

    def get_relatorio_profissionais(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_profissionais))
        input("Pressione Enter para Sair do Relatório de Profissionais")