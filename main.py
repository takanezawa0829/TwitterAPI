# -*- coding: utf-8 -*-
import config
import urllib.request
import datetime
from twitter import Twitter, OAuth

def main():
    global_ip_now = get_global_ip()
    global_ip_log = get_logs()

    if global_ip_now == global_ip_log:
        print('Global IPアドレスは変わっていません。')
        print('現在は、「' + global_ip_now + '」です。')
    else:
        print('Global IPアドレスが変更されました。')
        print('前回は、「' + global_ip_log + '」です。')
        print('現在は、「' + global_ip_now + '」です。')
        # 現在のIPアドレスをlogsに追記する。
        add_logs(global_ip_now)
        # Global IPアドレスの変更をツイートする。
        now = str(datetime.datetime.now()).split('.')[0]
        msg = f"TakanenServerのIPアドレスが更新されました。\nIPアドレス: {global_ip_now}\n更新日時: {now}"
        # ツイートする。
        send_msg(msg)

# ログの最後の行を取得する
def get_logs():
    f = open('logs', 'r')
    alltxt = f.readlines()
    f.close()
    endgyou = len(alltxt)
    ip_address = alltxt[endgyou-1].strip()

    return ip_address

# ログに追加する
def add_logs(msg):
    f = open('logs', 'a')
    f.write(msg + '\n')
    f.close()

# グローバルIPアドレスを取得
def get_global_ip():
    html = urllib.request.urlopen(config.URL).read().decode('utf-8')
    ip_address = html.split(': ')[1]
    ip_address = ip_address.split('<')[0]

    return ip_address

# ツイートする
def send_msg(msg):
    twi = Twitter(
        auth=OAuth(
            config.TW_TOKEN,
            config.TW_TOKEN_SECRET,
            config.TW_CONSUMER_KEY,
            config.TW_CONSUMER_SECRET,
        )
    )

    twi.statuses.update(status=msg)

if __name__ == "__main__":
    main()