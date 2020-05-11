# BiliBili-Data-acquisition
从BiliBili网页上爬取10000的用户信息和10000的视频信息分析课程设计
1 项目简介
bilibili视频数据分析

项目数据来自哔哩哔哩视频网站(https://www.bilibili.com/), 使用python简单的BeautifulSoup、Requests第三方库爬取数据。

2 爬虫脚本
crawl_users.py -- 用户数据爬虫

crawl_videos.py -- 视频数据爬虫(根据aid)

crawl_videos_keyword.py -- 视频数据爬虫(根据关键字)

3 其他工具脚本
covert_json_to_csv.py json -- 格式文件转换为csv文件

compute_videos_weight.py -- 不同视频热门程度的评价值

通过对每个视频中用户不同行为的评估, 计算出不同视频热门程度的评价值.

公式: 评价值 = 投币数 * 0.4 + 收藏数 * 0.3 + 弹幕数 * 0.4 + 回复数 * 0.4 + 点赞数 * 0.4 + 分享数 * 0.6 + 观看数 * 0.2

generate_random_aids.py -- 生成若干随机aid
