import os
from time import sleep

import requests
from lxml import etree

url = 'http://www.xbiquge.la/xiaoshuodaquan/'

headers = {
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
}

all_book_r = requests.get(url, headers=headers)
all_book_html = etree.HTML(all_book_r.content.decode('utf-8'))
all_book_url = all_book_html.xpath('//div[@class="novellist"]/ul/li/a/@href')
all_book_title = all_book_html.xpath('//div[@class="novellist"]/ul/li/a/text()')
print(all_book_url)
find_book = input('输入想下载的书名:')
num = 0
for book_title in all_book_title:
    if find_book == book_title:
        print('找到了，您要的', book_title)
        book_url = all_book_url[num]
        book_r = requests.get(book_url, headers=headers)
        book_html = etree.HTML(book_r.content.decode('utf-8'))
        book_url = book_html.xpath('//div[@id="list"]/dl/dd/a/@href')
        chapter_title = book_html.xpath('//div[@id="list"]/dl/dd/a/text()')
        judge = os.path.exists('../小说/%s' % str(book_title))
        if not judge:     
          os.makedirs('../小说/%s' % str(book_title))
        print('<------请输入数字(该小说共有%s章)------>' % len(chapter_title))
        download_book_start = int(input('输入从第几章开始下载：'))
        download_book_end = int(input('输入到第几章结束：'))
        chapter_num = 0
        for book_content_url in book_url[download_book_start - 1:download_book_end]:
            sleep(2)
            new_book_content_url = 'http://www.xbiquge.la' + book_content_url
            book_content_r = requests.get(new_book_content_url, headers=headers)
            book_content_html = etree.HTML(book_content_r.content.decode('utf-8'))
            book_content = book_content_html.xpath('//div[@class="box_con"]/div[@id="content"]/text()')
            with open('../小说/%s/%s.text' % (str(book_title), chapter_title[download_book_start + chapter_num -1]), 'w', encoding='utf-8') as write_content:
                all_content = ''
                for content in book_content:
                    all_content += content
                write_content.write(all_content)
                print(chapter_title[download_book_start + chapter_num -1], '--下载成功')
                chapter_num += 1
        print('全部下载完成')
        break
    elif num + 1 == len(all_book_title):
        print('查无此书')
    num += 1

