# coding:utf8
# html页面下载器
import urllib2

class HtmlDownLoader(object):

    def download(self, url):
        if url is None:
            return

        response = urllib2.urlopen(url)

        if response.getcode() != 200:
            return

        return response.read()