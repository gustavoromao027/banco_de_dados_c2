MENU_PRINCIPAL = """Menu Principal
1 - Relatórios
2 - Inserir
3 - Atualizar
4 - Remover
5 - Sair
"""

MENU_RELATORIOS = """Relatórios
1 - Relatório de Pacientes com Profissionais
2 - Relatório de Pacientes
3 - Relatório de Profissionais
0 - Sair
"""

MENU_ENTIDADES = """Entidades
1 - PACIENTES
2 - PROFISSIONAIS
"""

# Consulta de contagem de registros por tabela
QUERY_COUNT = 'select count(1) as total_{tabela} from {tabela}'

def clear_console(wait_time:int=3):
    '''
       Esse método limpa a tela após alguns segundos
       wait_time: argumento de entrada que indica o tempo de espera
    '''
    import os
    from time import sleep
    sleep(wait_time)
    os.system("clear")