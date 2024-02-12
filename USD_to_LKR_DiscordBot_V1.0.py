import time
import requests
from bs4 import BeautifulSoup
from discord_webhook import DiscordWebhook
from datetime import datetime

url = "https://www.google.com/finance/quote/USD-LKR?sa=X&ved=2ahUKEwj__Y_x166AAxUhSWwGHYgYAEUQmY0JegQIBhAr"
webhook_url = "webhook_url"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

current_date = datetime.now().strftime("%d.%m.%y")
current_time = datetime.now().strftime("%H:%M:%S")

last_rate = 0

def alert_discord(rate):
    message = f"@everyone\n **USD to LKR Bot Notify Every Change v1.0**\n Date: {current_date}\n Time: {current_time}\n USD to LKR Rate: **{{:.2f}}".format(float(rate)) + "**\n"
    discord_webhook = DiscordWebhook(url=webhook_url, content=message)
    discord_webhook.execute()

while True:
    print("Fetching Rate...")
    response = requests.get(url, headers=headers)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    rate = soup.find('div', class_='YMlKec fxKbKc').text
    
    print("Checking Rate...")
    if last_rate != rate:
        print("Found Difference, Sending Discord")
        alert_discord(rate)
    else:
        print("No Difference Found")

    last_rate = rate
    
    print("Waiting 15 mins...")
    time.sleep(900)
