import os


def read_file(filename):
    dirname = os.getcwd()
    dirname = dirname + '\\resources\data_files\\'
    filepath = dirname + filename
    with open(filepath, 'r') as fileref:
        return fileref.readlines()


def parse_data(raw_data):
    rows = []
    for i in raw_data:
        row = i.strip().split(',')
        rows.append(row)
    return rows


def get_data(filename):
    raw_data = read_file(filename)
    parsed_data = parse_data(raw_data)
    return parsed_data
