from model.profissionais import Profissional
from conexion.oracle_queries import OracleQueries

class Controller_Profissional:
    def __init__(self):
        pass
        
    def inserir_profissional(self) -> Profissional:
        ''' Ref.: https://cx-oracle.readthedocs.io/en/latest/user_guide/plsql_execution.html#anonymous-pl-sql-blocks'''
        
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuario o novo LICENÇA
        licenca = input("Licença Profissional (Novo): ")

        if self.verifica_existencia_profissional(oracle, licenca):
            # Solicita ao usuario o novo nome
            nome = input("Nome (Novo): ")
            # Solicita ao usuario o novo valor conusulta
            especialidade = input("Especialidade (Novo): ")
            # Solicita ao usuario o novo valor conusulta
            contato_envio = input("Contato (Novo): ") 
            # Insere e persiste o novo profissional
            oracle.write(f"insert into profissionais values ('{licenca}', '{nome}', '{especialidade}', '{contato_envio}')")
            # Recupera os dados do novo profissional criado transformando em um DataFrame
            bd_profissional = oracle.sqlToDataFrame(f"select licenca, nome, especialidade, contato_envio from profissionais where licenca = '{licenca}'")
            # Cria um novo objeto profissional
            novo_profissional = Profissional(bd_profissional.licenca.values[0], bd_profissional.nome.values[0], bd_profissional.especialidade.values[0], bd_profissional.contato_envio.values[0])
            # Exibe os atributos do novo profissional
            print(novo_profissional.to_string())
            # Retorna o objeto novo_profissional para utilização posterior, caso necessário
            return novo_profissional
        else:
            print(f"A Licença {licenca} já está cadastrado.")
            return None

    def atualizar_profissional(self) -> Profissional:
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o código do profissional a ser alterado
        licenca = int(input("Licença do profissional que deseja atualizar: "))

        # Verifica se o profissional existe na base de dados
        if not self.verifica_existencia_profissional(oracle, licenca):
            # Solicita ao usuario o novo nome
            novo_nome = input("Nome (Novo): ")  
            # Solicita ao usuario o novo valor conusulta
            novo_especialidade = input("Especialidade (Novo): ")
            # Solicita ao usuario o novo valor conusulta
            novo_contato_envio = input("Contato (Novo): ")

            # Atualiza o nome do profissional existente
            oracle.write(f"update profissionais set nome = '{novo_nome}', especialidade = '{novo_especialidade}', contato_envio = '{novo_contato_envio}'  where licenca = {licenca}")
            # Recupera os dados do novo profissional criado transformando em um DataFrame
            bd_profissional = oracle.sqlToDataFrame(f"select licenca, nome, valor_consulta from profissionais where licenca = {licenca}")
            # Cria um novo objeto profissional
            profissional_atualizado = Profissional(bd_profissional.licenca.values[0], bd_profissional.nome.values[0], bd_profissional.especialidade.values[0], bd_profissional.contato_envio.values[0])
            # Exibe os atributos do novo profissional
            print(profissional_atualizado.to_string())
            # Retorna o objeto profissional para utilização posterior, caso necessário
            return profissional_atualizado
        else:
            print(f"A Licença {licenca} não existe.")
            return None
        
    def excluir_profissional(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário a Licença do Profissional a ser alterado
        licenca = int(input("A licença do Profissional que irá excluir: "))        

        # Verifica se o medico existe na base de dados
        if not self.verifica_existencia_medico(oracle, licenca):            
            # Recupera os dados do novo medico criado transformando em um DataFrame
            bd_profissional = oracle.sqlToDataFrame(f"select crm, nome, valor_consulta from medicos where crm = {licenca}")
            # Revome o medico da tabela
            oracle.write(f"delete from agendamentos where licenca = {licenca}")    
            oracle.write(f"delete from profissionais where licenca = {licenca}")            
            # Cria um novo objeto profissional para informar que foi removido
            profissional_excluido = Profissional(bd_profissional.licenca.values[0], bd_profissional.nome.values[0], bd_profissional.especialidade.values[0], bd_profissional.contato_envio.values[0])
            # Exibe os atributos do profissional excluído
            print("Profissional Removido com Sucesso!")
            print(profissional_excluido.to_string())
        else:
            print(f"A licenca {licenca} não existe.")

    def verifica_existencia_profissional(self, oracle:OracleQueries, licenca:str=None) -> bool:
        # Recupera os dados do novo medico criado transformando em um DataFrame
        bd_profissional = oracle.sqlToDataFrame(f"select licenca, nome, especialidade, contato_envio from medicos where crm = {licenca}")
        return bd_profissional.empty