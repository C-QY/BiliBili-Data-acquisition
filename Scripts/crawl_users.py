import requests
import json
import time

headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'}


# 一个用户数据有两个来源, 所以要两个url用同时爬取
def generate_urls():
    """返回若干两个url列表的元组"""
    urls = []
    urls2 = []
    for m in range(50, 350):
        for i in range(m * 100, (m + 1) * 100):
            url = 'https://api.bilibili.com/x/web-interface/card?mid=' + str(i) + '&jsonp=jsonp&article=true'
            url2 = 'https://api.bilibili.com/x/space/acc/info?mid=' + str(i) + '&;jsonp=jsonp'
            urls.append(url)
            urls2.append(url2)
    return urls, urls2


def crawl(urls, urls2):
    """爬取用户数据"""
    factor = 0  # 减慢速度, 防止封ip
    users = []
    for url, url2 in zip(urls, urls2):
        res = requests.get(url, headers=headers)
        my_json = res.json()
        info = my_json['data']
        user = {}
        # id
        user['mid'] = info['card']['mid']
        # 昵称
        user['name'] = info['card']['name']
        # 性别
        user['sex'] = info['card']['sex']
        # 等级
        user['level'] = info['card']['level_info']['current_level']
        # 关注数
        user['friend'] = info['card']['friend']
        # 粉丝数
        user['fans'] = info['card']['fans']
        # 地点
        user['place'] = info['card']['place']

        res = requests.get(url2, headers=headers)
        my_json = res.json()
        info = my_json['data']

        if info is None:
            continue
        # 生日
        user['birthday'] = info['birthday']

        users.append(user)
        if factor % 6 == 0:
            time.sleep(2)
        factor += 1
    return users


def write(filename, data):
    """以json格式写入文件"""
    fp = open(filename, 'w+', encoding='utf-8')
    users_json = json.dumps(data, ensure_ascii=False)
    fp.write(users_json)


if __name__ == "__name__":
    output_file = 'data/users.txt'
    urls, urls2 = generate_urls()
    users = crawl(urls, urls2)
    write(users, output_file)

