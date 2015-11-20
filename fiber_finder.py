import getpass
import urllib


from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup

browser = webdriver.Firefox()
browser.get('http://switchtosmithville.com/check-availability/')

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
                    addr_input = browser.find_element_by_id('street_address')
                    addr_input.send_keys(out['address'])
                    city_input = browser.find_element_by_id('city')
                    city_input.send_keys(out['city'])
                    zip_input = browser.find_element_by_id('zip')
                    zip_input.send_keys(out['zip'])
                    #with urllib.request.urlopen('http://switchtosmithville.com/check-availability/') as smith_response:
                    #    smith_html = smith_response.read()
                    #    smith_parse = BeautifulSoup(smith_html, 'html.parser')
                    #    for link in smith_parse.find_all('div'):
                    #        print(link)
                    #css = browser.find_element_by_css_selector("div.input.map-calculate-button[value='Submit']")
                    #css = browser.find_element_by_css_selector("div.map-calculate-button[value='Submit']")

                    #link = browser.find_element_by_xpath(u'div//a[contains(text(), "Submit")]')
                    #link.click()
                    #submit = browser.find_element_by_class_name('map-form')
                    #submit = browser.find_element_by_class_name('map-calculate button')
                    #inputs = browser.find_elements_by_class_name('map-calculate button')
                    #submit.click()
                    #print(inputs)
                    #print(out)
                    #css.click()
                    ids = browser.find_elements_by_xpath('//*[@class]')
                    for ii in ids:
                    #print ii.tag_name
                        if ii.get_attribute('class').startswith('map-calculate'):
                            print(ii.get_attribute('class'))
                            ii.click()
                        #ii.submit()
                        print(ii.get_attribute('class'))
                    #submit =
                    break

        except AttributeError as err:
            print(err)
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