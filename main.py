from pybit.unified_trading import HTTP
from slack_sdk.webhook import WebhookClient
from dotenv import load_dotenv
load_dotenv()
import os


client = HTTP(testnet=False, api_key=os.getenv('BYBIT_API_KEY'), api_secret=os.getenv('BYBIT_API_SECRET'))

# ティッカーを取得
tickers = client.get_tickers(category="inverse")

# 配列の中身を表示
for ticker in tickers['result']['list']:
    print("銘柄名: " + ticker['symbol'])
    print("現在価格: $" + str(ticker['lastPrice']))
    print("24時間出来高: $" + str(ticker['volume24h']))
    print("---")