import os
from core import log
from dotenv import dotenv_values

ENV_FILE = ".env"
DEFAULT_CONFIG = {
    "VERBOSE": "False",
    "APP_RUNNING": "True",
    "PORT": "48001",
    "AIM_IP": "0.0.0.0",
    "AIM_PORT": "48000",
    "DEFAUT_TIMEOUT": "5",
    "HELLO_TIMEOUT": "5",
    "BOT_INTERVAL": "3"
}

if not os.path.exists(ENV_FILE):
    with open(ENV_FILE, "w") as file:
        for key, value in DEFAULT_CONFIG.items():
            file.write(f"{key}={value}\n")
    log(f"Arquivo {ENV_FILE} não encontrado. Gerado com os valores padrão do CEDRI.")

settings = {
    **DEFAULT_CONFIG,
    **dotenv_values(ENV_FILE)
}