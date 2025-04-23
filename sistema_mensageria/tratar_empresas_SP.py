import os
import pandas as pd

# Caminho do ficheiro de Estabelecimentos descompactado
entrada = os.path.join('dados-publicos\K3241.K03200Y0.D50111.ESTABELE')

# Caminho do ficheiro de saída
saida = "estabelecimentos_SP.csv"

# Nomes das colunas oficiais do layout da Receita
colunas = [
    "CNPJ_BASICO", "CNPJ_ORDEM", "CNPJ_DV", "IDENTIFICADOR_MATRIZ_FILIAL", 
    "NOME_FANTASIA", "SITUACAO_CADASTRAL", "DATA_SITUACAO_CADASTRAL", 
    "MOTIVO_SITUACAO_CADASTRAL", "NOME_CIDADE_EXTERIOR", "PAIS", 
    "DATA_INICIO_ATIVIDADE", "CNAE_PRINCIPAL", "CNAE_SECUNDARIOS", 
    "TIPO_LOGRADOURO", "LOGRADOURO", "NUMERO", "COMPLEMENTO", 
    "BAIRRO", "CEP", "UF", "MUNICIPIO", "DDD_1", "TELEFONE_1", 
    "DDD_2", "TELEFONE_2", "DDD_FAX", "FAX", "EMAIL", "SITUACAO_ESPECIAL", 
    "DATA_SITUACAO_ESPECIAL"
]

# Apaga ficheiro de saída se já existir
if os.path.exists(saida):
    os.remove(saida)

print(f"🔍 A processar: {entrada}")

encontrou = False

# Ler por partes para poupar memória
for chunk in pd.read_csv(entrada, sep=';', names=colunas, chunksize=100_000, encoding='latin1', low_memory=False):
    chunk.columns = chunk.columns.str.strip()

    filtrado = chunk[chunk['UF'] == 'SP']

    if not filtrado.empty:
        encontrou = True
        filtrado = filtrado.drop_duplicates()
        filtrado.to_csv(saida, mode='a', index=False, header=not os.path.exists(saida))

if encontrou:
    print(f"✅ Concluído! Dados de SP guardados em: {saida}")
else:
    print("⚠️ Nenhuma linha com UF == 'SP' encontrada.")
