"""
Pipeline ETL simples para consolidacao de vendas.

Etapas:
1. Extracao dos arquivos JSON.
2. Transformacao com calculo de KPI.
3. Carga em CSV e/ou Parquet.
"""

import glob
import os
import pandas as pd

from log.utils_log import log_decorator, tempo_execucao_decorator


@log_decorator
def extrair_dados_json(path: str) -> pd.DataFrame:
    """
    Extrai dados de varios arquivos JSON e consolida em um DataFrame.

    Step-by-step:
    1. Busca todos os arquivos com extensao `.json` no diretorio `path`.
    2. Le cada arquivo JSON em um DataFrame usando `pd.read_json`.
    3. Junta todos os DataFrames em um unico DataFrame com `pd.concat`.
    4. Retorna o DataFrame consolidado com indice reiniciado (`ignore_index=True`).
    """
    arquivos_json = glob.glob(os.path.join(path, "*.json"))
    df_lista = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_tratado = pd.concat(df_lista, ignore_index=True)
    return df_tratado

@log_decorator
def calcular_kpi_total_vendas(df_consolidado: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula o KPI de total vendido para cada linha do DataFrame.

    Step-by-step:
    1. Usa as colunas `Quantidade` e `Venda`.
    2. Multiplica os valores linha a linha.
    3. Salva o resultado na nova coluna `Total vendido`.
    4. Retorna o DataFrame atualizado.
    """
    df_consolidado["Total_vendido"] = (
        df_consolidado["Quantidade"] * df_consolidado["Venda"]
    )
    return df_consolidado

@log_decorator
def carregar_dados(df_entrada: pd.DataFrame, formato_saida: list[str]) -> None:
    """
    Salva o DataFrame final nos formatos solicitados.

    Step-by-step:
    1. Percorre a lista `formato_saida`.
    2. Se encontrar `csv`, salva como `dados_vendas.csv`.
    3. Se encontrar `parquet`, salva como `dados_vendas.parquet`.
    4. Finaliza sem retorno explicito.
    """
    for formato in formato_saida:
        formato_normalizado = formato.strip().lower()

        if formato_normalizado == "csv":
            df_entrada.to_csv("dados_vendas.csv")
        elif formato_normalizado == "parquet":
            df_entrada.to_parquet("dados_vendas.parquet")

@tempo_execucao_decorator
@log_decorator
def pipeline_calcular_kpi_vendas(path: str, formato_saida: list[str]) -> None:
    """
    Orquestra o fluxo ETL completo.

    Step-by-step:
    1. Extrai e consolida os JSONs com `extrair_dados_json`.
    2. Calcula o KPI com `calcular_kpi_total_vendas`.
    3. Carrega os dados finais com `carregar_dados`.
    4. Finaliza sem retorno explicito.
    """
    df_tratado = extrair_dados_json(path)
    df_kpi_vendas = calcular_kpi_total_vendas(df_tratado)
    carregar_dados(df_kpi_vendas, formato_saida)
