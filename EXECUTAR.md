#  GUIA COMPLETO - TRATAMENTO DE DADOS DE ESTABELECIMENTOS SP

## 📋 PRÉ-REQUISOS
1.**Python 3.11** 
2. [Instalar Anaconda ] (Windows/macOS/Linux)
3. Memória RAM: 4GB+
4. Espaço em disco: 500MB+

## 🛠️ CONFIGURAÇÃO INICIAL
```bash

# 1. Criar ambiente vazio
conda create -n becomex python=3.11.12
conda activate becomex

# 2. Instalar dependências críticas via Conda
conda install -c conda-forge pyarrow=19.0.1 pandas=2.2.3 numpy=2.2.4

# 3. Ativar ambiente
conda activate empresas-sp


# 4. Instalar demais pacotes via pip
pip install -r requirements.txt --no-deps

# 5. Verificar instalação
conda list

▶️ EXECUÇÃO PASSO-A-PASSO
🔵 Passo 1: Filtrar dados de SP

```bash

executar: tratar_empresas_sp.py
Resultado:
- estabelecimentos_SP.csv

🔵 Passo 2: Limpeza dos dados

bash
rodar o arquivo jupyter notebook notebooks/cleaning_estabelecimentos.ipynb

## No notebook:

- Execute todas as células (Shift+Enter)

- Verifique os outputs

- Feche o notebook após conclusão

**Resultados finais:**

estabelecimentos_SP_limpos.csv.gz

estabelecimentos_SP_limpos.parquet


⚠️ SOLUÇÃO DE PROBLEMAS COMUNS
🔴 Erro: "PyArrow não encontrado"

Solução: conda install -c conda-forge pyarrow

🔴 Dependências do pip não encontradas
pip install --upgrade numpy==2.2.4 pandas==2.2.3

🔴 Dados corrompidos

# Verificação rápida:
import pandas as pd
df = pd.read_parquet('data/processed/estabelecimentos_SP_limpos.parquet')
print(df.info())

📌 COMANDOS ÚTEIS
# Reconstruir ambiente (se corrompido)
conda env remove -n becomex
conda env create -f environment.yml

# Desativar ambiente
conda deactivate

# Listar ambientes
conda env list

# Atualizar dependências
conda env update -f environment.yml --prune