import logging

logging.basicConfig(level=logging.DEBUG, filename="ejemplo_logs.log", filemode="w")

logging.debug("Log de debugging")
logging.info("Log informativo")
logging.warning("Log de advertencia")
logging.error("Log de error")
logging.critical("Log de error crítico")
