import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7417268851:AAEvku2tmMQ2H8pw2XFJR7wvajSNpOtoMRA")

    APP_ID = int(os.environ.get("APP_ID", "2170492"))

    API_HASH = os.environ.get("API_HASH", "82b683da442942d5c177ec520318a32f")
