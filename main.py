import gdown
import csv
import os
i = {
    'campus': 2,
    'curso': 4,
    'turno': 5,
    'profs': 8,
    'tituloProj': 9,
    'descricao': 11,
    #tentar dos dois links
    'link1': 14,
    'link2': 15,
    'permissao1': 18,
    'permissao2': 19,
    #a partir daqui, ir até o final da lista pegando todos os valores diferentes de ''
    #Alternância nome, RA, nesta ordem
    'integrantesAPartirDe': 21

}
def adjustURLForDownload(url):
    if 'view' in url:
        indiceInicial = url.index('/d/') + 3
        indiceFinal  = url.rindex ('/')
        id = url[indiceInicial:indiceFinal]
        print (f'https://drive.google.com/uc?id={id}')
        return f'https://drive.google.com/uc?id={id}'
    elif 'folders' in url:
        indiceInicial = url.index('/folders/') + 8
        indiceFinal  = url.rindex ('?')
        id = url[indiceInicial:indiceFinal]
        print (f'https://drive.google.com/uc?id={id}')
        return f'https://drive.google.com/uc?id={id}'
    else:
        return url.replace('open', 'uc')


def isGoogleDriveLink (url):
    return 'drive' in url

def contains_digit (s):
    return any(map(str.isdigit, s))

def montaEquipe (linha):
    result = 'Equipe: '
    for elemento in linha[i['integrantesAPartirDe']:len(linha) - 4]:
        if elemento != '' and not contains_digit(elemento) and elemento != "N/D":
            result += elemento.title() + ','
    result = result[0:len(result) - 1]
    return result
with open(r'dados.csv', encoding='utf-8') as csvfile:
    cont = 0
    leitor = csv.reader(csvfile, delimiter=',')
    for linha in leitor:
        try:    
            #criar pasta para esse grupo
            tituloProjeto = f'{linha[i["tituloProj"]].strip().replace(":", "-")}'
            tituloProjeto = tituloProjeto.replace('"', '').replace('|', '-').replace('/','-').replace('*','.')
            if not os.path.exists(f'grupos/{tituloProjeto}'):
                os.makedirs(f'grupos/{tituloProjeto}')
            #cria arquivo com titulo, integrantes etc
            if not os.path.exists(f'grupos/{tituloProjeto}/dados.txt'): 
                arquivo = open(f'grupos/{tituloProjeto}/dados.txt', 'w')
                print ('**********************')
                #download do video
                url = linha[i['link1']] if len( linha[i['link1']]) >=2 else  linha[i['link2']]
                if len(url) >=2 and isGoogleDriveLink(url):
                    print(url)
                    adjustedURL = adjustURLForDownload(url)
                    print (adjustedURL)
                    arquivo.writelines (url)
                    arquivo.writelines ('\n')
                    arquivo.writelines (adjustedURL)
                    gdown.download (url=adjustedURL, output=f'grupos/{tituloProjeto}/video.mp4', quiet=False)
        except Exception as e:
            print (e)