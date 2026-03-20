from functools import wraps
from sys import stderr
from time import perf_counter
from typing import Any

from loguru import logger

# Removendo os handlers existentes para evitar duplicacao
logger.remove()

# Configuracao do logger para stderr
logger.add(
    sink=stderr,
    format="{time} <r>{level}</r> <g>{message}</g> {file}",
    level="INFO",
)

# Configuracao do logger para arquivo de log
logger.add(
    r"log\logs_etl.log",
    format="{time} {level} {message} {file}",
    level="INFO",
)


def _resumir_resultado(nome_funcao: str, result: Any) -> str:
    if result is None:
        mensagens_sem_retorno = {
            "carregar_dados": (
                "concluida com sucesso. Arquivos de saida exportados "
                "(sem retorno explicito)."
            ),
            "pipeline_calcular_kpi_vendas": (
                "concluida com sucesso. Pipeline ETL finalizado "
                "(sem retorno explicito)."
            ),
        }
        return mensagens_sem_retorno.get(
            nome_funcao,
            "concluida com sucesso (sem retorno explicito).",
        )

    if hasattr(result, "shape") and hasattr(result, "columns"):
        linhas, colunas = result.shape
        return (
            "retornou DataFrame com "
            f"{linhas} linhas, {colunas} colunas e colunas={list(result.columns)}"
        )

    return f"retornou {result!r}"


def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Chamando funcao '{func.__name__}' com args {args} e kwargs {kwargs}")
        try:
            result = func(*args, **kwargs)
            logger.info(f"Funcao '{func.__name__}' {_resumir_resultado(func.__name__, result)}")
            return result
        except Exception as e:
            logger.exception(f"Excecao capturada em '{func.__name__}': {e}")
            raise  # Re-lanca a excecao para nao alterar o comportamento da funcao decorada

    return wrapper


def tempo_execucao_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        inicio = perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            duracao_segundos = perf_counter() - inicio
            logger.info(
                "Tempo de execucao da funcao '{}': {:.3f}s",
                func.__name__,
                duracao_segundos,
            )

    return wrapper
