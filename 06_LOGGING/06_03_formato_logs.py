import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%H:%M:%S"
)

nombre = "Paco"
logging.error(f"{nombre} creó el error")

logging.warning("Log de advertencia")
logging.error("Log de error")
logging.critical("Log de error crítico")

try:
    division = 2 / 0
except:
    logging.exception("División por cero")
