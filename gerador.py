import pandas as pd
import random
from datetime import datetime, timedelta

# Definindo as colunas
colunas = ['Projeto', 'Atividade', 'Responsável', 'Data Inicial', 'Data Final', 'Dias de Duração', 'Dias de Execução', 'Valor Orçamento', 'Valor Gasto', 'Status']

# Definindo os projetos
projetos = [f'Projeto {i}' for i in range(1, 16)]

# Definindo responsáveis
responsaveis = ['Ana', 'Carlos', 'Beatriz', 'Daniel', 'Elisa', 'Fábio', 'Gisele', 'Henrique', 'Isabela', 'João']

# Criando um DataFrame com base na quantidade de atividades variável
dados = []
for projeto in projetos:
    quantidade_atividades = random.randint(3, 10)  # No mínimo 3 atividades por projeto
    for atividade in range(1, quantidade_atividades + 1):
        nome_atividade = f'Tarefa {atividade}'
        responsavel = random.choice(responsaveis)

        # Gerando datas aleatórias em 2023
        data_inicial = datetime(2023, 1, 1) + timedelta(days=random.randint(0, 364))
        duracao = random.randint(2, 20)  # Dias de duração entre 2 e 20
        data_final = data_inicial + timedelta(days=duracao)

        # Definindo dias de execução (aleatório entre 2 e 20)
        dias_execucao = random.randint(2, 20)

        # Definindo Valor Orçamento (mínimo 10000, máximo 200000)
        valor_orcamento = random.randint(10000, 200000)

        # Definindo Valor Gasto (aleatório, mas não ultrapassar o Valor Orçamento)
        valor_gasto = random.uniform(0.8, 1.0) * valor_orcamento  # Valor Gasto entre 80% e 100% do Valor Orçamento

        # Definindo o Status com base nas condições fornecidas
        if dias_execucao < duracao:
            status = 'Em Andamento'
        elif dias_execucao > duracao:
            status = 'Finalizado'
        else:
            status = 'Não Iniciado'

        # Formatando as datas
        data_inicial_str = data_inicial.strftime('%Y-%m-%d')
        data_final_str = data_final.strftime('%Y-%m-%d')

        linha = [projeto, nome_atividade, responsavel, data_inicial_str, data_final_str, duracao, dias_execucao, valor_orcamento, valor_gasto, status]
        dados.append(linha)

# Criando o DataFrame
dataset = pd.DataFrame(dados, columns=colunas)

# Exportando o DataFrame para um arquivo Excel
nome_arquivo_excel = 'dataset_projeto.xlsx'
dataset.to_excel(nome_arquivo_excel, index=False)

print(f'O dataset foi exportado para o arquivo Excel: {nome_arquivo_excel}')
