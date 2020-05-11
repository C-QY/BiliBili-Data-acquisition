import pandas as pd


def compute_weight(filename):
    """通过对每个视频中用户不同行为的评估, 计算出不同视频热门程度的评价值"""
    df = pd.read_json(filename, encoding='utf-8')
    df = df[~(df.view == '--')]  # view列可能包含'--'值, 导致该行无法计算评价值, 因而这里直接删除这些行

    # 评价值 = 投币数 * 0.4 + 收藏数 * 0.3 + 弹幕数 * 0.4 + 回复数 * 0.4 + 点赞数 * 0.4 + 分享数 * 0.6 + 观看数 * 0.2
    weight = df.coin*0.4 + df.favorite*0.3 + df.danmaku*0.4 + df.reply*0.4 + df.like*0.4 + df.share*0.6 + df.view*0.2

    df.loc[:, 'weight'] = weight  # 将计算得到的评估值加入最后一列
    return df


if __name__ == '__main__':
    df = compute_weight('data/vedios.txt')
    df.to_csv('weight.csv', index=False, encoding='utf-8')