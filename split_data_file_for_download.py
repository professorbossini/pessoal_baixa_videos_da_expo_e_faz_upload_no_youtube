import csv
with open(r'dados.csv', encoding='utf-8') as csvfile:
    cont = 1
    leitor = csv.reader(csvfile, delimiter=',')
    for linha in leitor:
        nome_arquivo = f'dados{cont}.csv'
        arquivo = open(nome_arquivo, 'a', encoding='utf-8')        
        if cont % 20 != 0:
            arquivo.writelines (f'{linha}\n')
        else:
            cont += 1
