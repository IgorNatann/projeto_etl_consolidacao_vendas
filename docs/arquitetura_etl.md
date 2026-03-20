# Arquitetura ETL

## Fluxo end-to-end

1. `extrair_dados_json(path)`
2. `calcular_kpi_total_vendas(df_consolidado)`
3. `carregar_dados(df_entrada, formato_saida)`
4. `pipeline_calcular_kpi_vendas(path, formato_saida)`

## Funcoes e responsabilidades

### `extrair_dados_json(path)`

- localiza arquivos `*.json` no diretorio de entrada
- le cada arquivo com Pandas
- consolida os dados em um unico DataFrame

### `calcular_kpi_total_vendas(df_consolidado)`

- calcula a coluna `Total_vendido`
- formula: `Quantidade * Venda`

### `carregar_dados(df_entrada, formato_saida)`

- exporta `dados_vendas.csv` quando o formato inclui `csv`
- exporta `dados_vendas.parquet` quando o formato inclui `parquet`
- usa normalizacao de formato (`strip().lower()`)

### `pipeline_calcular_kpi_vendas(path, formato_saida)`

- orquestra todas as etapas do ETL
- recebe parametros de entrada e formatos de saida
- e o ponto principal monitorado em tempo de execucao

## Ponto de entrada

`pipeline/pipeline.py` define:

- `PATH_DADOS = "data"`
- `FORMATO_SAIDA = ["csv", "parquet"]`

Depois chama `pipeline_calcular_kpi_vendas(PATH_DADOS, FORMATO_SAIDA)`.
