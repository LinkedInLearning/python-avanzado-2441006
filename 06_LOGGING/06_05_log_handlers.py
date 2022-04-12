import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

handler_consola = logging.StreamHandler()
formato_logs = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler_consola.setFormatter(formato_logs)
logger.addHandler(handler_consola)

handler_archivo = logging.FileHandler("archivo.log")
handler_archivo.setLevel(logging.ERROR)
handler_archivo.setFormatter(formato_logs)
logger.addHandler(handler_archivo)

logger.info("registro informativo")

