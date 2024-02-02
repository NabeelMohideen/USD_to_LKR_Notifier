import time
import requests
from bs4 import BeautifulSoup
from discord_webhook import DiscordWebhook
from datetime import datetime

url = "https://www.google.com/finance/quote/USD-LKR?sa=X&ved=2ahUKEwj__Y_x166AAxUhSWwGHYgYAEUQmY0JegQIBhAr"
webhook_url = "webhook url"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

current_date = datetime.now().strftime("%d-%m-%Y")
current_time = datetime.now().strftime("%H:%M:%S")

last_rate = 0

def alert_discord(rate):
    message = f"@everyone\n **USD to LKR Bot Notify Every Change v1.0**\n Date: {current_date}\n Time: {current_time}\n USD to LKR Rate: **{{:.2f}}".format(float(rate)) + "**\n"
    discord_webhook = DiscordWebhook(url=webhook_url, content=message)
    discord_webhook.execute()

while True:
    response = requests.get(url, headers=headers)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    rate = soup.find('div', class_='YMlKec fxKbKc').text
    
    if last_rate is not None and last_rate != rate:
        alert_discord(rate)

    last_rate = rate
    time.sleep(900)