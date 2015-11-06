import getpass
import urllib


from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup

#browser = webdriver.Firefox()
#browser.get('http://trulia.com')

bloom = 'Bloomington, IN'
iu = '107 S. Indiana Avenue'

bloom_zip_min = 47401
bloom_zip_max = 47408
out = {}

url = 'http://www.trulia.com/for_sale/{}_zip/'.format(str(bloom_zip_min))
with urllib.request.urlopen(url) as response:
    html = response.read()
    parsed_site = BeautifulSoup(html, 'html.parser')
    for link in parsed_site.find_all('meta'):
        result = link.get('content')
        try:
            if type(result) != None or type(result) != NoneType:
                if result.startswith('/property/'):
                    result = result.split('/')[2]
                    result = result.split('-')
                    out['zip'] = str(result[-1])
                    out['state'] = result[-2]
                    out['city'] = result[-3]
                    out['address'] = ' '.join(result[1:-2])
                    print(out)

        except AttributeError as err:
            print('LOL', err)
            #if 'property' in result:
            #    print(result)
#        if link.get('content').startswith('/property'):
#            result = link.get('content')
#            result = result.split('/')
#            print(result)

    #print(parsed_site.prettify())


'''
if __name__ == '__main__':
    pass
'''