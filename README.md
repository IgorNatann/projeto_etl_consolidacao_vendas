# Projeto ETL - Consolidacao de Vendas

Mini-case de ETL em Python para consolidar arquivos JSON de vendas e gerar saidas em CSV e Parquet.

Este projeto foi pensado para ser simples, didatico e reutilizavel como base para estudos e portfolio.

## Para quem este projeto e

- Quem esta comecando em Python.
- Quem quer entender ETL na pratica.
- Quem quer um projeto pequeno para portfolio tecnico.

## O que este projeto faz

1. Le varios arquivos JSON de vendas.
2. Consolida tudo em um unico DataFrame.
3. Calcula o KPI `Total_vendido` (`Quantidade * Venda`).
4. Salva os dados finais em `dados_vendas.csv` e/ou `dados_vendas.parquet`.

## Estrutura do projeto

```text
projeto_etl_consolidacao_vendas/
|-- .venv/                  # ambiente virtual local (ignorado no Git)
|-- .qodo/                  # arquivos locais de ferramenta (ignorado no Git)
|-- .pytest_cache/          # cache local de testes
|-- .gitignore
|-- README.md
|-- requirements.txt
|-- pyproject.toml          # arquivo local (ignorado no Git)
|-- data/
|   |-- coleta_dia01.json
|   |-- coleta_dia02.json
|   |-- coleta_dia03.json
|-- etl/
|   |-- etl.py
|-- pipeline/
|   |-- pipeline.py
|-- dados_vendas.csv        # gerado ao executar a pipeline (ignorado no Git)
|-- dados_vendas.parquet    # gerado ao executar a pipeline (ignorado no Git)
```

## Tecnologias usadas

- Python
- Pandas
- JSON (entrada)
- CSV e Parquet (saida)

## Como rodar (passo a passo)

1. Crie e ative um ambiente virtual (opcional, recomendado).
2. Instale as dependencias:

```bash
pip install -r requirements.txt
```

3. Execute a pipeline:

```bash
python -c "from etl.etl import pipeline_calcular_kpi_vendas; pipeline_calcular_kpi_vendas('data', ['csv', 'parquet'])"
```

4. Confira os arquivos gerados na raiz do projeto:
- `dados_vendas.csv`
- `dados_vendas.parquet`

## Logica do ETL (step-by-step)

### 1) Extracao - `extrair_dados_json(path)`

1. Busca todos os arquivos `*.json` na pasta informada.
2. Le cada arquivo com `pd.read_json`.
3. Junta os DataFrames com `pd.concat`.
4. Retorna um DataFrame consolidado.

### 2) Transformacao - `calcular_kpi_total_vendas(df_consolidado)`

1. Usa as colunas `Quantidade` e `Venda`.
2. Calcula `Total_vendido = Quantidade * Venda`.
3. Retorna o DataFrame com a nova coluna.

### 3) Carga - `carregar_dados(df_entrada, formato_saida)`

1. Recebe os formatos desejados (ex.: `['csv', 'parquet']`).
2. Salva CSV quando o formato for `csv`.
3. Salva Parquet quando o formato for `parquet`.

### 4) Orquestracao - `pipeline_calcular_kpi_vendas(path, formato_saida)`

1. Chama a extracao.
2. Chama a transformacao.
3. Chama a carga.

## Exemplo rapido em Python

```python
from etl.etl import pipeline_calcular_kpi_vendas

pipeline_calcular_kpi_vendas("data", ["csv", "parquet"])
```

## Proximos passos (ideias de melhoria)

- Adicionar validacao de colunas obrigatorias.
- Tratar cenario de pasta sem arquivos JSON.
- Adicionar testes automatizados.
- Adicionar logs para monitorar a execucao.
