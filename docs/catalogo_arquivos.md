# Catalogo de Arquivos

Resumo dos arquivos principais do projeto e de sua finalidade.

| Caminho | Tipo | Funcao |
|---|---|---|
| `README.md` | doc | pagina principal com resumo e links para a documentacao modular |
| `docs/README.md` | doc | indice de navegacao da documentacao |
| `docs/arquitetura_etl.md` | doc | descreve arquitetura e fluxo ETL |
| `docs/observabilidade.md` | doc | detalha logging, decorators e rastreabilidade |
| `docs/execucao.md` | doc | passo a passo de instalacao, execucao e saidas |
| `docs/catalogo_arquivos.md` | doc | inventario dos arquivos importantes |
| `etl/etl.py` | codigo | etapas de extracao, transformacao, carga e orquestracao |
| `pipeline/pipeline.py` | codigo | entrypoint local para executar a pipeline |
| `log/utils_log.py` | codigo | configuracao do `loguru` e decorators de observabilidade |
| `log/logs_etl.log` | artefato | arquivo de logs com trilha da execucao |
| `data/*.json` | dados | arquivos de entrada para a pipeline |
| `dados_vendas.csv` | saida | resultado da carga em CSV |
| `dados_vendas.parquet` | saida | resultado da carga em Parquet |
| `requirements.txt` | dependencia | bibliotecas necessarias para rodar o projeto |
