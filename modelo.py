# Instala as bibliotecas firebase-admin
!pip install firebase-admin

# Importa a biblioteca principal do Firebase Admin SDK
import firebase_admin

# Importa o módulo de credenciais para autenticação
from firebase_admin import credentials

# Importa o módulo Firestore para interagir com o banco de dados NoSQL
from firebase_admin import firestore

# Importa o módulo Storage para gerenciar o armazenamento de arquivos
from firebase_admin import storage

# Importa o módulo datetime para manipulação de datas e horas
import datetime
# Define o caminho para o arquivo de credenciais do Firebase (um arquivo JSON)
file_path = ''

# Cria um objeto de credenciais a partir do arquivo JSON especificado
cred = credentials.Certificate(file_path)
# Inicializa o aplicativo Firebase com as credenciais e configura o bucket de armazenamento
firebase_admin.initialize_app(cred, {
    'storageBucket': 'datapipe-97e03.appspot.com'  # Especifica o bucket de armazenamento do Firebase
})
# Cria um cliente Firestore para interagir com o banco de dados
db = firestore.client()

# Obtém uma referência ao bucket de armazenamento do Firebase
bucket = storage.bucket()
# Define uma função para ler arquivos do armazenamento do Firebase
def read_files_from_storage():
    # Lista todos os arquivos (blobs) no bucket de armazenamento
    blobs = bucket.list_blobs()  
    
    # Itera sobre cada blob (arquivo) encontrado
    for blob in blobs:
        # Faz o download do conteúdo do arquivo como texto
        file_content = blob.download_as_text()
        
        # Chama a função process_file para processar o conteúdo do arquivo e o nome do blob
        process_file(file_content, blob.name)

# Define uma função para processar o conteúdo de um arquivo
def process_file(contents, file_name):
    # Divide o conteúdo do arquivo em linhas
    linhas = contents.split('\n')
    
    # Itera sobre cada linha do conteúdo
    for linha in linhas:
        # Cria um dicionário com dados transformados
        data_transformada = {
            'projeto': 'Datapipe',  # Nome do projeto
            'data_linha': {'linha': linha},  # Armazena a linha atual em um dicionário
            'tag': 'tag1',  # Uma tag associada ao dado
            'data_ingestao': datetime.datetime.utcnow().isoformat()  # Data e hora da ingestão em formato ISO
        }
        # Chama a função para salvar os dados transformados no Firestore
        salvar_no_firestore(data_transformada)
# Define uma função para salvar dados no Firestore
def salvar_no_firestore(data):
    try:
        # Adiciona os dados à coleção 'projetos' no Firestore
        db.collection('projetos').add(data)
        
        # Imprime uma mensagem de sucesso com os dados salvos
        print('Documento salvo com sucesso:', data)
    except Exception as e:
        # Se ocorrer um erro, imprime uma mensagem de erro
        print('Erro ao salvar documento:', e)

#importa a bibliotecas pandas
import pandas as pd

# Função para ler arquivos CSV e armazenar os dados em variáveis
def ler_csv_e_armazenar(file_names):
    dados = {}  # Dicionário para armazenar os dados

    for file_name in file_names:
        # Lê o arquivo CSV usando pandas
        df = pd.read_csv(file_name)
        
        # Armazena os dados em uma variável com o nome do arquivo (sem a extensão)
        dados[file_name.split('.')[0]] = df  # Armazena o DataFrame

    return dados

# Lista dos arquivos CSV que você deseja ler
arquivos_csv = ['arquivo1.csv', 'arquivo2.csv']  # Substitua pelos seus arquivos

# Chama a função e armazena os dados
dados_armazenados = ler_csv_e_armazenar(arquivos_csv)

# Exemplo de como imprimir os dados de cada arquivo
for nome, df in dados_armazenados.items():
    print(f'Dados de {nome}:')
    print(df)  # Imprime o DataFrame correspondente
