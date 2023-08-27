from pybit.unified_trading import HTTP
from slack_sdk.webhook import WebhookClient
from dotenv import load_dotenv
load_dotenv()
import os

webhook = WebhookClient(os.getenv('SLACK_URL'))



client = HTTP(testnet=False, api_key=os.getenv('BYBIT_API_KEY'), api_secret=os.getenv('BYBIT_API_SECRET'))
tickers = client.get_tickers(category="inverse")

# 配列の中身を表示
for ticker in tickers['result']['list']:
    response = webhook.send(text="銘柄名: " + ticker['symbol'] + "\n現在価格: $" + str(ticker['lastPrice']) + "\n24時間出来高: $" + str(ticker['volume24h']))