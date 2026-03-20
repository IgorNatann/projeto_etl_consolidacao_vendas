# Projeto ETL - Consolidacao de Vendas

Mini-case de ETL em Python para consolidar arquivos JSON de vendas, calcular KPI e gerar saidas em CSV/Parquet com observabilidade de execucao.

## Visao geral

O projeto entrega um fluxo ETL simples e rastreavel:

1. extrai arquivos JSON de `data/`
2. consolida em DataFrame
3. calcula `Total_vendido = Quantidade * Venda`
4. exporta em CSV e/ou Parquet
5. registra logs em `log/logs_etl.log`

## Ferramentas e tecnologias utilizadas

![status](https://img.shields.io/badge/status-em%20evolucao-yellow) ![linguagem](https://img.shields.io/badge/linguagem-Python%203.10%2B-blue) ![arquitetura](https://img.shields.io/badge/arquitetura-ETL-orange) ![pandas](https://img.shields.io/badge/processamento-Pandas-150458?logo=pandas&logoColor=white) ![pyarrow](https://img.shields.io/badge/engine-Parquet%20(pyarrow)-4B8BBE) ![loguru](https://img.shields.io/badge/logging-Loguru-00A98F)

- `Python`: linguagem principal da pipeline.
- `Pandas`: consolidacao dos dados e calculo do KPI.
- `PyArrow`: suporte para exportacao em Parquet.
- `Loguru`: observabilidade da execucao e tratamento de excecoes.
- `JSON`, `CSV` e `Parquet`: formatos de entrada e saida de dados.

## Documentacao modular

A documentacao foi separada para facilitar leitura e manutencao:

- [Mapa da documentacao](docs/README.md)
- [Arquitetura ETL](docs/arquitetura_etl.md)
- [Observabilidade e logs](docs/observabilidade.md)
- [Execucao e saidas](docs/execucao.md)
- [Catalogo de arquivos](docs/catalogo_arquivos.md)

## Quickstart

```bash
pip install -r requirements.txt
python pipeline/pipeline.py
```

## Evidencias de execucao

### Comando executado

```bash
python pipeline/pipeline.py
```

### Trecho do log

Arquivo: `log/logs_etl.log`

```text
2026-03-20T17:07:03.797628-0300 INFO Funcao 'calcular_kpi_total_vendas' retornou DataFrame com 9 linhas, 6 colunas e colunas=['Produto', 'Categoria', 'Quantidade', 'Venda', 'Data', 'Total_vendido'] utils_log.py
2026-03-20T17:07:03.815805-0300 INFO Funcao 'carregar_dados' concluida com sucesso. Arquivos de saida exportados (sem retorno explicito). utils_log.py
2026-03-20T17:07:03.815805-0300 INFO Funcao 'pipeline_calcular_kpi_vendas' concluida com sucesso. Pipeline ETL finalizado (sem retorno explicito). utils_log.py
2026-03-20T17:07:03.816326-0300 INFO Tempo de execucao da funcao 'pipeline_calcular_kpi_vendas': 0.035s utils_log.py
```

## Saidas esperadas

- `dados_vendas.csv`
- `dados_vendas.parquet`
- `log/logs_etl.log`
