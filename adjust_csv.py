# -*- coding=utf-8 -*-
import csv    #加载csv包便于读取csv文件


class Config(object):

    path = 'export.csv'  # 输入的CSV文件路径
    file_name = 'convert.csv'  # 格式转换后的CSV文件名称


def convert_to_sum(csv_reader_lines, file_name):
    data = []
    flag = 0
    for one_line in csv_reader_lines:
        if flag == 0:
            flag = 1
            pass

        else:
            data.append(one_line)    #将读取的csv分行数据按行存入列表‘date’中

    with open(file_name, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for i in data:
            for ii in i:
                writer.writerow([ii])
        f.close()


if __name__ == '__main__':
    obj = Config()
    csv_file = open(obj.path)
    csv_reader_lines = csv.reader(csv_file)
    convert_to_sum(csv_reader_lines, obj.file_name)
    csv_file.close()