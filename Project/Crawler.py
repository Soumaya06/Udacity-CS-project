__author__ = 'Raphael'
import urllib2
def getLink(page):
    start_link= page.find ("<a href=")
    start_quote= page.find ('"', start_link)
    end_quote= page.find ('"', start_quote+1)
    url= page [start_quote+1: end_qote]
    page= [end_quote:]
    return url
    
    return page


def get_all_links(page):
    """


    :rtype : list of all links in a page
    :param page: html content of the page
    """
page= ''
def get_all_links(page):
    links = []
    while True:
        url =extract_link(page)
        if url:
            links.append(url)
        else:
            break
    return links

return page


def get_page(url):
    """
    Hassane and Tolu
    :rtype : html conten of paget
    :param url of page to return:
    """
    response = urllib2.urlopen(url)
    return response.read()

def crawl_web(seed):
    """


    :rtype : a a list of crawled pagest
    :param seed: the starting linkk for crawling
    """
        to_crawl = [seed]
        crawled = []
        while to_crawl:
            page = to_crawl.pop()
            if page not in crawled:
                to_crawl.union(self.get_all_links(self.get_page(page)))
                crawled.append(page)

        return crawled
