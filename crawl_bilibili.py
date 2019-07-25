import requests
import re
import jieba
import numpy as np
from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt
 
def crawl_barrage(url):
	'''
	爬取弹幕
	input: str 弹幕链接
	return: list 弹幕列表
	'''
	response = requests.get(url)
	response.encoding = 'utf-8'

	if response.status_code == 200:
		print('获取到弹幕！')

		barrage_list = re.findall('">(.*?)</d>', response.text)
		return barrage_list
	else:
		print('获取弹幕失败！')

def save_txt_file(barrage_list, file_name):
	'''
	将数据存储到txt文件
	input: list, str 弹幕列表， 文件名
	return: none
	'''
	with open('{}.txt'.format(file_name), 'w', encoding='utf-8') as f:
		for row in barrage_list:
			f.write(row)
			f.write('\n')
		print('成功保存为{}.txt'.format(file_name))

def cut_word(file_path):
    """
    对数据分词
    input: str 文件名
    return: str 分词后的数据
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        barrage_txt = file.read()
        wordlist = jieba.cut(barrage_txt, cut_all=True)
        wl = " ".join(wordlist)
        print(wl)
        return wl

def cut_word(file_name):
    """
    对数据分词
    input: str 文件名
    return: str 分词后的数据
    """
    with open(file_name, 'r', encoding='utf-8') as file:
        barrage_txt = file.read()
        wordlist = jieba.cut(barrage_txt, cut_all=True)
        wl = " ".join(wordlist)
        print(type(wl))
        return wl

def create_word_cloud(text, wc_name):
    """
    生成词云
    input: str, str 生成词云的字符串, 保存的词云名字
    return: none
    """
    # 设置词云字体文件
    WC_FONT_PATH = r'C:\Windows\WinSxS\amd64_microsoft-windows-font-truetype-simhei_31bf3856ad364e35_10.0.17763.1_none_e4eda043cc3e4f50\simhei.ttf'

    # 数据清洗词列表
    stop_words = ['哈哈', '高能', '哈哈哈', '千万', '哈哈哈哈', '合影']
    # 设置词云的一些配置，如：字体，背景色，词云形状，大小
    wc = WordCloud(background_color="white", max_words=500, scale=4,
                   max_font_size=50, random_state=42, stopwords=stop_words, font_path=WC_FONT_PATH)
    # 生成词云
    wc.generate(text)

    # 在只设置mask的情况下,你将会得到一个拥有图片形状的词云
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.figure()
    plt.show()

    # 保存词云
    wc.generate('{}.jpg'.format(wc_name))

if __name__ == '__main__':
	cid = input('输入视频的cid: ')
	url = 'https://api.bilibili.com/x/v1/dm/list.so?oid={}'.format(cid)
	barrage_list = crawl_barrage(url)
	file_name = input('要保存的文件名: ')
	save_txt_file(barrage_list, file_name)
	barrage_text = cut_word('{}.txt'.format(file_name))
	create_word_cloud(barrage_text, cid)