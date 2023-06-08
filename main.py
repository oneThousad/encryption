import os
import random
import string
import sys


def randomString(length):
    letters = string.ascii_letters + string.digits
    result = ''.join(random.sample(letters, length))
    return result


if not os.path.exists('management.txt'):
    open('management.txt', 'w')
if input() == '1':
    file = open('management.txt', 'r')
    getword = input()
    if '%' in getword:
        print('사용할 수 없는 문자가 포함되어 있습니다.')
        sys.exit()
    dataSet = {}
    fileData = file.readlines()
    for data, i in zip(fileData, range(len(fileData))):
        prefix = data[:data.find(':')]
        change = data[data.find(':') + 2:]
        dataSet[prefix] = change.replace('\n', '')
        if prefix in getword:
            getword = getword.replace(prefix, f'%ch{i}')
    start = 0
    getword = getword + '%'
    for i in range(len(getword)):
        if i >= len(getword):
            break
        if getword[i] == '%':
            data = getword[start:i]
            if start == i or data == '' or '%ch' in data:
                start = i + 4
                continue
            getword = getword.replace(data, f'%ch{len(dataSet.values())}')
            dataSet[data] = randomString(len(data))
            start = i + 4
    getword = getword[:len(getword) - 1]
    write = ''
    for data, i in zip(dataSet.keys(), range(len(dataSet.keys()))):
        getword = getword.replace(f'%ch{i}', dataSet[data])
        write = write + f'{data}: {dataSet[data]}\n'
    file = open('management.txt', 'w')
    file.write(write)
    print(getword)
else:
    file = open('management.txt', 'r')
    getword = input()
    dataSet = {}
    fileData = file.readlines()
    for data, i in zip(fileData, range(len(fileData))):
        prefix = data[:data.find(':')]
        change = data[data.find(':') + 2:]
        dataSet[change.replace('\n', '')] = prefix
        getword = getword.replace(change.replace('\n', ''), f'%ch{i}')
    start = 0
    getword = getword + '%'
    for i in range(len(getword)):
        if i >= len(getword):
            break
        if getword[i] == '%':
            data = getword[start:i]
            if start == i or data == '' or '%ch' in data:
                start = i + 4
                continue
            getword = getword.replace(data, f'%ch{len(dataSet.values())}')
            start = i + 4
    getword = getword[:len(getword) - 1]
    for data, i in zip(dataSet.keys(), range(len(dataSet.keys()))):
        getword = getword.replace(f'%ch{i}', dataSet[data])
    print(getword)
