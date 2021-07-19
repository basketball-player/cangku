import PIL.Image as image
from wordcloud import WordCloud
import jieba
import os
import matplotlib.pyplot as plt

def trans_CN(text):
    # 接收分词的字符串
    word_list = jieba.cut(text)
    # 分词后在单独个体之间加上空格
    result = " ".join(word_list)
    return result

def create_wordcloud(str,name):
    #输入参数为要生成词云的字符串，以及保存的文件名

    #文本分词,
    text = trans_CN(str)

    #停用词库，路径应根据网站文件夹更改
    stopwords = set()
    content = [line.strip() for line in open('static/stopword_cn_2.txt','r',encoding='utf-8').readlines()]
    stopwords.update(content)

    #生成词云对象
    wordcloud = WordCloud(
        # 添加遮罩层
    #    mask=mask,
        # 生成中文字的字体,必须要加,不然看不到中文，路径根据网站文件更改
        font_path="static/font/simhei.ttf",
        stopwords=stopwords,
        height=800,
        width=800
    ).generate(text)

    #设置导出路径，应该根据网站文件夹更改。
    save_path = name+'.png'
    wordcloud.to_file(save_path)
    #print(save_path,"is done")


