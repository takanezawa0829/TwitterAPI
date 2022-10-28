import os
from dotenv import find_dotenv, load_dotenv

# Twitter設定
load_dotenv(find_dotenv())  # .envファイルを探して読み込む
TW_CONSUMER_KEY = os.environ.get('TW_CONSUMER_KEY')
TW_CONSUMER_SECRET = os.environ.get('TW_CONSUMER_SECRET')
TW_TOKEN = os.environ.get('TW_TOKEN')
TW_TOKEN_SECRET = os.environ.get('TW_TOKEN_SECRET')

# ダイナミックDNS設定
URL = os.environ.get('URL')