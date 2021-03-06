import os
import logging

"""
Yes, this is awful, Yes I'm too stubborn to use dotenv, I may open it as an
issue if people complain
"""


def get_secrets():
    secrets = {}
    env_file = "core/secrets.env"
    with open(env_file) as f:
        for line in f:
            if line.startswith("#") or not line.strip():
                continue
            if "export" not in line:
                continue
            key, value = line.replace("export ", "", 1).strip().split("=", 1)
            secrets[key] = value
        return secrets


def set_logging(level: str, filename: str = "discord.log") -> None:
    logger = logging.getLogger("discord")
    try:
        logger.setLevel(level)
    except ValueError:
        try:
            level = int(level)
            logger.setLevel(level)
        except Exception as e:
            logger.setLevel(logging.WARNING)
            print(f"EXCEPTION: {e}\n Going to Default")
    print(f"Logging set to {logging.getLevelName(logger.level)}")  # Least bougie setup

    handler = logging.FileHandler(filename=filename, encoding="utf-8", mode="w")
    handler.setFormatter(
        logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s")
    )
    logger.addHandler(handler)


VERSION = "1.1.0"
PREFIX = "!"
