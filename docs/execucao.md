# Execucao e Saidas

## Requisitos

- Python 3.10+ (recomendado)
- dependencias listadas em `requirements.txt`

## Instalacao

```bash
pip install -r requirements.txt
```

## Execucao

```bash
python pipeline/pipeline.py
```

## Artefatos gerados

- `dados_vendas.csv`
- `dados_vendas.parquet`
- `log/logs_etl.log`

## Personalizacao rapida

No arquivo `pipeline/pipeline.py`, altere:

- `PATH_DADOS` para apontar para outro diretorio de entrada
- `FORMATO_SAIDA` para escolher entre `csv` e `parquet`
