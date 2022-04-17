# Bloco de código contendo as chamadas de coleta dos dados (leitura dos arquivos),
# preparação e processamento dos dados

# Importa o processamento de csv para ler arquivos .csv
import csv

# Importa class Pessoa:
# Pessoa.index = Index, valor não representa nada por enquanto
# Pessoa.nome = Nome da pessoa
# Pessoa.idade = Idade da pessoa
from structure import Pessoa


# Função write_csv(table):
# Recebe inputs do console e salva numa tabela CSV.
# Util para criar a tabela CSV para fins de teste.
# Separa as variaveis por ',' e as entradas por linha
def write_csv(table_file):

    exit_flag = input("Pressione E para ir diretamente p/ leitura dos dados ou qualquer outra tecla para continuar... ")

    while exit_flag != 'e' and exit_flag != 'E':
        nome = input("Nome: ")
        idade = input("Idade: ")

        with open(table_file, 'a', newline='') as data_file:
            table = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            table.writerow([nome, idade])

        exit_flag = input("Deseja continuar? Pressione E para sair ou qualquer outra tecla para continuar... ")


# função print_table(table):
# Recebe uma tabela csv e apenas a imprime na tela.
# Usado para fins de teste.
def print_table(table_file):

    with open(table_file, 'r') as data_file:
        table = csv.reader(data_file, delimiter=',')
        line_count = 0

        for row in table:
            print(f'\nIndex: {line_count}')
            print(f'Nome: {row[0]}')
            print(f'Idade: {row[1]}')
            line_count += 1


# Função read_table_to_list(table):
# Recebe uma tabela csv e retorna uma lista de classe Pessoa.
# Cada entrada na lista é uma Pessoa. Ex: lista[0] = Pessoa
def read_table_to_list(table_file):

    lista = []                                                  # declara a lista a ser preenchida

    with open(table_file, 'r') as data_file:                    # abre o arquivo da tabela como read ('r')
        table = csv.reader(data_file, delimiter=',')            # le as variaveis separadas por ','
        line_count = 0                                          # zera contador (inutil, serve apenas pra usar de index)

        for row in table:                                       # row[0] = nome; row[1] = idade
            lista.append(Pessoa(line_count, row[0], row[1]))    # adiciona entrada no array
            line_count += 1                                     # rinse and repeat

    return lista                                                # retorna a lista[] com cada entrada sendo uma Pessoa
