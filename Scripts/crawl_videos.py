import requests
import json
import time
import numpy as np

headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'}


def get_urls(aid_file, size):
    """从已生成的aids.txt中截取一部分aid生成url用于爬取"""
    s = np.loadtxt(aid_file, dtype=int)
    urls = []
    for i in range(len(s[:size])):
        url = 'https://api.bilibili.com/x/web-interface/archive/stat?aid='+str(s[i])
        urls.append(url)
    return urls


def crawl(urls, size):
    """爬取视频数据"""
    factor = 0  # 减慢速度, 防止封ip
    videos = []
    for url in urls[0:size]:
        res = requests.get(url, headers=headers)
        my_json = res.json()
        info = my_json['data']
        video = {}
        if info is not None:
            # aid
            video['aid'] = info['aid']
            # 视频编码
            video['bvid'] = info['bvid']
            # 播放数
            video['view'] = info['view']
            # 弹幕数
            video['danmaku'] = info['danmaku']
            # 评论数
            video['reply'] = info['reply']
            # 收藏数
            video['favorite'] = info['favorite']
            # 硬币数
            video['coin'] = info['coin']
            # 转发数
            video['share'] = info['share']
            # 点赞数
            video['like'] = info['like']
            videos.append(video)
        if factor % 6 == 0:
            time.sleep(2)
        factor += 1
    return videos


def write(filename, data):
    """将数据以json格式将爬取数据写入filename文件"""
    fp = open(filename, 'w+', encoding='utf-8')
    users_json = json.dumps(data, ensure_ascii=False)
    fp.write(users_json)


if __name__ == "__main__":
    input_file = 'data/aids.txt'
    output_file = 'data/video.txt'
    size = 10000
    urls = get_urls(input_file, size)
    videos = crawl(urls, size)
    write(output_file, videos)
