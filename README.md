# 📊 PROJETO DE ANÁLISE DE ESTABELECIMENTOS COMERCIAIS DE SÃO PAULO

![Banner](https://example.com/banner-projeto-sp.jpg) **(adicione um banner relevante se disponível)*

## 📌 VISÃO GERAL
Pipeline de dados para tratamento e análise de estabelecimentos comerciais no estado de São Paulo, incluindo:

- **Filtragem** de dados brutos por UF (SP)
- **Limpeza** e padronização de registros
- **Exportação** para formatos otimizados (Parquet/CSV comprimido)

## 🛠 TECNOLOGIAS PRINCIPAIS
| Tecnologia       | Versão   | Uso Principal                |
|------------------|----------|------------------------------|
| Python           | 3.11.12  | Linguagem base               |
| Pandas           | 2.2.3    | Manipulação de dados         |
| PyArrow          | 19.0.1   | Formato Parquet              |
| Jupyter Notebook | 6.5.4    | Análise interativa           |

## 📂 ESTRUTURA DO PROJETO


## 🚀 COMEÇANDO

### Pré-requisitos
- Miniconda/Anaconda instalado
- Windows 10/11 (testado em build 19045+)
- 4GB RAM livre

### Instalação

# 1. Criar ambiente Conda
conda env create -f environment.yml

# 2. Ativar ambiente
conda activate becomex

📈 FLUXO DE PROCESSAMENTO
## Filtragem inicial:

bash
python src/tratar_empresas_sp.py

## Análise e limpeza:

bash
jupyter notebook notebooks/cleaning_estabelecimentos.ipynb