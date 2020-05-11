import json
import requests
import time
from bs4 import BeautifulSoup

headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'}


def generate_urls(keyword):
    """根据关键字生成url"""
    urls = []
    for i in range(1, 50):
        url = 'https://search.bilibili.com/all?keyword=' + keyword + '&page=' + str(i)
        urls.append(url)
    return urls


def crawl(urls):
    """爬取视频数据"""
    videos = []
    factor = 0  # 减慢速度, 防止封ip
    for url in urls[:1]:
        res = requests.get(url, headers=headers)
        bs = BeautifulSoup(res.text, 'html.parser')
        items = bs.find_all(class_="tags")
        for item in items:
            video = {}
            # 观看次数
            video['view'] = item.find(class_="so-icon watch-num").text.strip()
            # 弹幕数
            video['danmaku'] = item.find(class_="so-icon hide").text.strip()
            # 上传时间
            video['upload_time'] = item.find(class_="so-icon time").text.strip()
            # up主名
            video['up'] = item.find(class_='up-name').text
            videos.append(video)
        if factor % 3 == 0:
            time.sleep(3)
        factor += 1
    return videos


def write(filename, data):
    """将数据以json格式将爬取数据写入filename文件"""
    fp = open(filename, 'w+', encoding='utf-8')
    users_json = json.dumps(data, ensure_ascii=False)
    fp.write(users_json)


if __name__ == "__main__":
    keyword = 'A'
    output_file = 'data/video.txt'

    urls = generate_urls(keyword)
    videos = crawl(urls)
    write(output_file, videos)
