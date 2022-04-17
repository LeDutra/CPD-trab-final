# Função principal

# Importa o arquivo auxiliar processing.py com as funções de procesamento
import processing as proc

# Define o nome do arquivo da 'tabela' .csv
table = 'table.csv'

# proc.write_csv(table)                           # função de teste com input manual pra testar escritas na tabela
# proc.print_table(table)                         # função de teste de print da tabela de arquivo .csv

lista = proc.read_table_to_list(table)          # chama função que converte tabela csv para lista ordenada

for Pessoa in lista:
    print(Pessoa.nome, Pessoa.idade)
