# 📬 Projeto Sistema de Mensageria

Este projeto implementa um sistema de mensageria utilizando Python. Foi desenvolvido com foco em modularidade, testes e facilidade de uso.

## 📁 Estrutura do Projeto


## ⚙️ Tecnologias Utilizadas

- Python 3.10+
- Conda (opcional)
- Bibliotecas: `pandas`, `requests`

## 🚀 Como Executar

### 1. Clonar o repositório

```bash
git clone https://github.com/felipetamiozzo/ProjetoSistemaMensageria.git
cd ProjetoSistemaMensageria

2. Criar ambiente (opcional)
bash

conda env create -f environment.yaml
conda activate mensageria

Ou instalar via pip:

bash

pip install -r requirements.txt

3. Executar o filtro de dados de São Paulo
python tratar_empresas_SP.py

4. Executar o tratamento e limpeza dos dados
Abrir e correr o notebook:

bash

jupyter notebook cleaning_estabelecimentos.ipynb
Este notebook realiza limpeza de colunas, tratamento de valores nulos e salva os dados em .csv e .parquet.

⚙️ Dados Utilizados
Fonte Oficial
Dataset: Estabelecimentos0 (parte do arquivo K3241.K03200Y0.D50111.ESTABELE).

Origem: Dados Abertos da Receita Federal (2025-01).

Descrição: Contém informações cadastrais de estabelecimentos comerciais no Brasil (ex: CNPJ, endereço, CNAE, situação cadastral).

Por que os dados não estão no repositório?
Os arquivos originais são muito grandes (ex: Estabelecimentos0 tem ~XX GB).

Política do GitHub: Limite de arquivos acima de 100MB.

Direitos de uso: Os dados são públicos, mas redistribuição em massa não é recomendada.