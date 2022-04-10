# Bloco de código contendo as chamadas de coleta dos dados (leitura dos arquivos),
# preparação e processamento dos dados

import csv


def write_table(table_file):

    exit_flag = input("Pressione E para ir diretamente p/ leitura dos dados ou qualquer outra tecla para continuar... ")

    while exit_flag != 'e' and exit_flag != 'E':
        nome = input("Nome: ")
        idade = input("Idade: ")

        with open(table_file, 'a', newline='') as data_file:
            table = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            table.writerow([nome, idade])

        exit_flag = input("Deseja continuar? Pressione E para sair ou qualquer outra tecla para continuar... ")


def read_table(table_file):

    with open(table_file, 'r') as data_file:
        table = csv.reader(data_file, delimiter=',')
        line_count = 0

        for row in table:
            print(f'\nIndex: {line_count}')
            print(f'Nome: {row[0]}')    # row[0] = Nome
            print(f'Idade: {row[1]}')   # row[1] = Idade
            line_count += 1
