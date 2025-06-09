import requests
import time
from telegram import Bot

# Configuration
BIRDEYE_API_KEY = 'e8279c21c47c406793882f1cdad49fb3'
TELEGRAM_TOKEN = '7609723485:AAHU3lSexvutrcWBXqbVLzermO9q7WdZCW8'
CHAT_ID = '1071883968'

# Critères de sélection
MIN_LIQUIDITY = 10000
MIN_VOLUME_24H = 30000
MIN_HOLDERS = 50
RECENT_TIME_LIMIT_MIN = 15

bot = Bot(token=TELEGRAM_TOKEN)


# Fonction de récupération des meme coins depuis Birdeye
def fetch_meme_coins():
    url = f"https://public-api.birdeye.so/public/solana/recent_tokens?sort_by=created&sort_type=desc&limit=50&offset=0"
    headers = {"X-API-KEY": BIRDEYE_API_KEY}
    response = requests.get(url, headers=headers)
    return response.json().get("data", [])


# Vérification des critères et notification Telegram
def notify_new_coins():
    coins = fetch_meme_coins()
    for coin in coins:
        created_at = coin.get('createdAt', 0) / 1000
        current_time = time.time()
        minutes_since_created = (current_time - created_at) / 60

        if minutes_since_created > RECENT_TIME_LIMIT_MIN:
            continue

        liquidity = coin.get("liquidity", 0)
        volume = coin.get("volume24hUSD", 0)
        holders = coin.get("holderCount", 0)

        if (liquidity >= MIN_LIQUIDITY and
                volume >= MIN_VOLUME_24H and
                holders >= MIN_HOLDERS):
            message = (
                f"🚀 Nouveau meme coin détecté !\n\n"
                f"Nom : {coin.get('name')}\n"
                f"Symbole : {coin.get('symbol')}\n"
                f"Liquidité : ${liquidity}\n"
                f"Volume 24h : ${volume}\n"
                f"Nombre de holders : {holders}\n"
                f"Lien : https://birdeye.so/token/{coin.get('address')}"
            )
            bot.send_message(chat_id=CHAT_ID, text=message)


# Lancement périodique du bot
while True:robot.send_message(chat_id=ID_CHAT, text="✅ Le bot a bien démarré et est en ligne !")
    notify_new_coins()
    time.sleep(60)  # Vérifie chaque minute
