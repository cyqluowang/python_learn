import jieba
from collections import Counter

'''
统计词语出现的次数
自动分词， 需要一个文件
'''

no_char = [",", "。", ".", ":", "\"", "'", "!", "，", "\n", "“", "、", "”", "》", "《"]
with open("test.txt", "r", encoding='utf8') as file:
    f = file.read()
    print(f)
    seg_list = jieba.cut(str(f), cut_all=False)
    seg_list_result = []
    for line in seg_list:
        if line in no_char:
            print(line)
            continue
        else:
            seg_list_result.append(line)
    print(Counter(seg_list_result))



