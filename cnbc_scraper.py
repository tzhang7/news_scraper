# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import random
import time
import socket
import http.client

URL = 'https://www.cnbc.com/2019/12/10/jack-nicklaus-gold-rolex-watch-sells-for-1-million-at-auction.html'
#URL = 'https://www.cnbc.com/2019/12/11/goldman-sachs-sees-a-pretty-attractive-play-for-indonesian-rupiah.html'


def get_cnbc_news():
    header = {
        'authority': 'www.cnbc.com',
        'method': 'GET',
        'path': '/2019/12/10/jack-nicklaus-gold-rolex-watch-sells-for-1-million-at-auction.html',
        'scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8',
        'cache-control': 'max-age=0',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
    }

    timeout = random.choice(range(80, 180))

    try:
        rep = requests.get(URL, headers=header, timeout=timeout)
        rep.encoding = 'utf-8'
    except socket.timeout as e:
        print(e)
        time.sleep(random.choice(range(8, 15)))
    except socket.error as e:
        print(e)
        time.sleep(random.choice(range(8, 15)))
    except http.client.BadStatusLine as e:
        print('5:', e)
        time.sleep(random.choice(range(30, 80)))

    except http.client.IncompleteRead as e:
        print('6:', e)
        time.sleep(random.choice(range(5, 15)))

    html_text = rep.text

    # Parse data using beautifulSoup
    bs = BeautifulSoup(html_text, 'html.parser')
    body = bs.body
    title = body.find_all('h1', class_='ArticleHeader-headline')[0].text
    publish_time = body.find_all('div', class_='ArticleHeader-time')[0].text
    kd = body.find_all('div', class_='group')
    kd_list = [x.text for x in kd]
    key_points = kd_list[0]
    contents = '\n'.join(kd_list[1:])

    print("Title:{0}".format(title))
    print("Publish Time:{0}".format(publish_time))
    print("Key points:{0}".format(key_points))
    print("Contents:{0}".format(contents))


if __name__ == '__main__':
    get_cnbc_news()
