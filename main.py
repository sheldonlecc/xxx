import jieba
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 读取停用词文件
try:
    with open('D:\stopwords.txt', 'r', encoding='utf-8') as f:
        # 读取每一行并去除首尾空格，然后添加到集合中
        stopwords = {line.strip() for line in f.readlines()}
except FileNotFoundError:
    print("停用词文件未找到，请检查路径。")
    # 若文件未找到，使用默认的停用词集合
    stopwords = {
        '的', '了', '是', '吗', '在', '我', '你', '他', '我们', '这', '那',
        '就', '也', '还', '不', '都', '吧', '啊', '哦', '呢', '啦', '吗', '跟', "哈哈", '看',
        '有', '很', '哈哈哈哈', '这个', '说', '给', '能', '个', '星星', '眼', '附议', '笑', '哭', '回复', '和', '多', '一个', '那个'
    }

# 判断是否为中文字符
def is_chinese_char(c):
    return '\u4e00' <= c <= '\u9fff'

# 读取弹幕文件
try:
    with open('D:/弹幕.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
except FileNotFoundError:
    print("文件未找到，请检查路径。")
    exit()

# 处理中文分词
words = []
for line in lines:
    # 分词并过滤
    seg = jieba.cut(line.strip())
    words.extend([
        word for word in seg if len(word) >= 1 and word not in stopwords and word.strip() and all(
            is_chinese_char(c) for c in word)
    ])

# 统计词频
word_counter = Counter(words)
top20 = word_counter.most_common(20)

# 输出结果
print("词频前20的词语：")
for word, count in top20:
    print(f"{word}: {count}")
    print("hello")