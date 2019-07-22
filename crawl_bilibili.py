import requests
import re

def crawl_barrage(url):
	'''
	爬取弹幕
	input: str 弹幕链接
	output: list 弹幕列表
	'''
	response = requests.get(url)
	response.encoding = 'utf-8'

	barrage_list = re.findall('">(.*?)</d>', response.text)

	return barrage_list

def save_txt_file(barrage_list, file_name):
	'''
	将数据存储到txt文件
	input: list, str 弹幕列表， 文件名
	output: none
	'''
	with open('{}.txt'.format(file_name), 'w', encoding='utf-8') as f:
		for row in barrage_list:
			f.write(row)
			f.write('\n')

if __name__ == '__main__':
	url = 'https://api.bilibili.com/x/v1/dm/list.so?oid=104240398'
	barrage_list = crawl_barrage(url)
	save_txt_file(barrage_list, '弹幕')

