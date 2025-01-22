#Kymang

import os

from dotenv import load_dotenv

load_dotenv(".env")


BOT_TOKEN = os.environ.get("BOT_TOKEN", "7995709523:AAEb9tfsVdDQKdKuikfB2yxP7hPk5NkzMlA")
API_ID = int(os.environ.get("API_ID", "27826569"))
API_HASH = os.environ.get("API_HASH", "16d4e33ea8d9f7160b61b228c18b5829")
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://stanlev:stanlev@cluster0.lpzo6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
ADMINS = [int(x) for x in (os.environ.get("ADMINS", "1734774709").split())]
MEMBER = [int(x) for x in (os.environ.get("MEMBER", "160").split())]
LOG_GRP = int(os.environ.get("LOG_GRP", "-1002061778178"))
BOT_ID = int(os.environ.get("BOT_ID", "7995709523"))

KITA = [int(x) for x in (os.environ.get("KITA", "1734774709").split())]
