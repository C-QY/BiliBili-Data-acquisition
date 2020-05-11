import pandas as pd


def convert(json_filename, csv_filename):
    """将json文件转换为csv文件"""
    df = pd.read_json(json_filename, encoding='utf-8')
    df.to_csv(csv_filename, index=False, encoding='utf-8')


if __name__ == '__main__':
    input_file = 'data/input.txt'
    output_file = 'data/output.csv'
    convert(input_file, output_file)
