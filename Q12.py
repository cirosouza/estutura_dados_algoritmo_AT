import os

def lista_arquivos(diretorio):

    try:
        itens = os.listdir(diretorio)
        for item in itens:
            caminho_longo = os.path.join(diretorio, item)

            if os.path.isdir(caminho_longo):
                # Continua a busca em subdiretórios
                lista_arquivos(caminho_longo)
            else:
                # Exibe apenas arquivos
                print(f"[ARQUIVO] {caminho_longo}")

    except PermissionError:
        print(f"Permissão negada: {diretorio}")
    except FileNotFoundError:
        print(f"Diretório não encontrado: {diretorio}")
    except Exception as e:
        print(f"Ocorreu um erro ao acessar: {diretorio}")


DIRETORIO_TESTE = r"D:\software_engineering\blocos_e_cursos\ciencia_da_computacao\estrutura_dados_algoritmo"

lista_arquivos(DIRETORIO_TESTE)