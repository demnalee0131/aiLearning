# 遍历一个文件夹下所有的.txt文件，统计总行数和出现频率最高的10个词

import re


path = r'C:\dev\testTxt\test.txt'

def remove_punctuation(value):
    return re.sub(r'[^a-zA-Z\u4e00-\u9fff]', '', value)

clean_ops = [str.strip, remove_punctuation, str.lower]

def clean_strings(strings, ops):
    result = []
    for value in strings:
        for func in ops:
            value = func(value)
        result.append(value)
    return result

word_count = {}

with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    total_lines = len(lines)

    for line in lines:
        cleaned_words = clean_strings(line.split(), clean_ops)
        for word in cleaned_words:
            word_count[word] = word_count.get(word, 0) + 1

top_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:10]

print(f'Total lines: {total_lines}')
print('Top 10 words:')
for word, count in top_words:
    print(f'{word}: {count}')