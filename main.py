# Função principal

import processing as proc                       # importa o arquivo auxiliar structure.py
table = 'table.csv'                             # define o arquivo da tabela utilizada para armazenamento em .csv


proc.write_table(table)                         # função temporária com input manual pra testar escritas na tabela
proc.read_table(table)                          # função de leitura da tabela de arquivo .csv

# array = proc.read_table_to_array(table)       # incompleto


