# -*- coding: utf-8 -*-
from baike-python import url_manager,html_downloader,html_parser,html_outputer

class SpiderMain(object);
    def __init__(self):
        '''
        构造函数初始化
        '''
        self.urls = url_manager.UrlManger()
        self.downloader = html_downloader.HtmlDownload()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self,root_url):
        '''
        爬虫调度方法
        '''
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d : %s' % (count,new_url)
                html_cont = self.downloader.download(new_url)
                new_urls,new_data = self.parser.parse(new_url,html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if count == 1000:
                    break
                count += 1
            except:
                print 'craw failed'

        self.outputer.output_html()

def main():
    # 入口 url
    root_url = 'https://baike.baidu.com/item/Python/407313'
    spider = SpiderMain()
    spider.craw(root_url)

if __name__ == '__main__':
    main()