import json

filename = 'Result/result_json/sort.json'
with open('Result/result_json/local.json', 'r', encoding='utf-8-sig', errors='ignore') as json_file:
    data = json.load(json_file, strict=False)

err = 5
# flag = 0


def col_apart():
    flag = 0
    n = 1
    data.sort(key=lambda x: x["x1"])
    print(data)
    data2 = json.dumps(data, indent=4, ensure_ascii=False)
    with open(filename, 'w') as f:
        f.write(data2)
    for i in range(len(data)-1):
        a = int(data[i]['x1'])
        b = int(data[i - 1]['x1'])
        if (abs(int(data[i+1]['x1']) - int(data[i]['x1'])) > err):
            e = int(data[i]['x1']) - int(data[i - 1]['x1'])
            if flag == 1:
                n = n + 1
                flag = 0
            data[i + 1]['start_col'] = n
            data[i]['start_col'] = n - 1
            # data[i]['x2']
        else:
            data[i]['start_col'] = n
            flag = 1

    data[len(data) - 1]['start_col'] = n

    n = 1
    data.sort(key=lambda x: x["x2"])
    for i in range(len(data) - 1):
        if (abs(int(data[i + 1]['x2']) - int(data[i]['x2'])) > err):
            e = int(data[i]['x2']) - int(data[i - 1]['x2'])
            if flag == 1:
                n = n + 1
                flag = 0
            data[i + 1]['end_col'] = n
            data[i]['end_col'] = n - 1
            # data[i]['x2']
        else:
            data[i]['end_col'] = n
            flag = 1

    data[len(data) - 1]['end_col'] = n

    data2 = json.dumps(data, indent=4, ensure_ascii=False)
    with open(filename, 'w') as f:
        f.write(data2)


# 行
def row_apart():
    flag = 0
    n = 1
    data.sort(key=lambda x: x["y1"])
    for i in range(len(data) - 1):
        if (abs(int(data[i + 1]['y1']) - int(data[i]['y1'])) > err):
            if flag == 1:
                n = n + 1
                flag = 0
            data[i+1]['start_row'] = n
            data[i]['start_row'] = n - 1
        else:
            data[i]['start_row'] = n
            flag = 1

    data[len(data) - 1]['start_row'] = n

    n = 1
    data.sort(key=lambda x: x["y2"])
    print(data)
    for i in range(len(data) - 1):
        num = i
        id = data[i]['id']
        if (abs(int(data[i + 1]['y2']) - int(data[i]['y2'])) > err):
            a = int(data[i]['y1'])
            b = int(data[i - 1]['y1'])
            if flag == 1:
                n = n + 1
                flag = 0
            data[i + 1]['end_row'] = n
            data[i]['end_row'] = n - 1
        else:
            data[i]['end_row'] = n
            flag = 1

    data[len(data) - 1]['end_row'] = n

    data2 = json.dumps(data, indent=4, ensure_ascii=False)
    with open(filename, 'w') as f:
        f.write(data2)


col_apart()
row_apart()

