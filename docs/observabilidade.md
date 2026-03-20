# Observabilidade e Logs

## Logger configurado

A configuracao fica em `log/utils_log.py` e usa `loguru` com dois destinos:

- `stderr`
- arquivo `log/logs_etl.log`

## Decorators

### `log_decorator`

Responsabilidades:

- registrar chamada de funcao com `args` e `kwargs`
- registrar retorno da funcao
- registrar excecao com stack trace em caso de erro
- melhorar leitura para retorno `None` e `DataFrame`

### `tempo_execucao_decorator`

Responsabilidades:

- medir duracao total com `perf_counter()`
- registrar tempo mesmo quando ocorre excecao (`finally`)

## Aplicacao no ETL

A funcao `pipeline_calcular_kpi_vendas` usa os dois decorators com a ordem:

```python
@tempo_execucao_decorator
@log_decorator
def pipeline_calcular_kpi_vendas(...):
    ...
```

Com essa ordem, o log traz rastreabilidade por etapa e tempo total da pipeline.

## Exemplo de sequencia no arquivo de log

```text
INFO Chamando funcao 'pipeline_calcular_kpi_vendas' ...
INFO Chamando funcao 'extrair_dados_json' ...
INFO Funcao 'extrair_dados_json' retornou DataFrame com ...
INFO Chamando funcao 'calcular_kpi_total_vendas' ...
INFO Funcao 'calcular_kpi_total_vendas' retornou DataFrame com ...
INFO Chamando funcao 'carregar_dados' ...
INFO Funcao 'carregar_dados' concluida com sucesso ...
INFO Funcao 'pipeline_calcular_kpi_vendas' concluida com sucesso ...
INFO Tempo de execucao da funcao 'pipeline_calcular_kpi_vendas': ...s
```

## Evidencias de execucao

### Comando executado

```bash
python pipeline/pipeline.py
```

### Trecho real do arquivo de log

Arquivo: `log/logs_etl.log`

```text
2026-03-20T17:07:03.797628-0300 INFO Funcao 'calcular_kpi_total_vendas' retornou DataFrame com 9 linhas, 6 colunas e colunas=['Produto', 'Categoria', 'Quantidade', 'Venda', 'Data', 'Total_vendido'] utils_log.py
2026-03-20T17:07:03.815805-0300 INFO Funcao 'carregar_dados' concluida com sucesso. Arquivos de saida exportados (sem retorno explicito). utils_log.py
2026-03-20T17:07:03.815805-0300 INFO Funcao 'pipeline_calcular_kpi_vendas' concluida com sucesso. Pipeline ETL finalizado (sem retorno explicito). utils_log.py
2026-03-20T17:07:03.816326-0300 INFO Tempo de execucao da funcao 'pipeline_calcular_kpi_vendas': 0.035s utils_log.py
```
