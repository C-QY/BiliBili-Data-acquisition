import numpy as np


def generate_random_aids(size, output_file):
    """生成指定个数aid的txt文件"""
    aids = np.arange(1, size + 1)
    np.random.shuffle(aids)
    with open(output_file, 'w') as f:
        for i in range(len(aids)):
            f.write(str(aids[i]) + '\n')


if __name__ == '__main__':
    size = 50000
    filename = 'data/aids.txt'
    generate_random_aids(size, filename)
