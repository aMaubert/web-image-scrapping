from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup


class Browser:

    def __init__(self, webdriverUrl, max_images, key_word):
        self.webdriverUrl = webdriverUrl
        if max_images is not None and max_images > 0 :
            self.max_images = max_images
        else :
            self.max_images = 50
        self.searchUrl = []
        self.searchUrl.append('https://www.bing.com/images/search?q=' + key_word)
        self.searchUrl.append('https://www.google.fr/search?hl=fr&' \
                         'q='+ key_word + '&'\
                         'tbm=isch')




    def launchSearch(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        browser = webdriver.Chrome(self.webdriverUrl, options=options)
        browser.set_window_size(1280, 1024)

        all_downloadable_url = []
        for eachSearchUrl in self.searchUrl :

            browser.get(eachSearchUrl)

            element = browser.find_element_by_tag_name('body')

            # Scroll down
            for i in range(27) :
                element.send_keys(Keys.PAGE_DOWN)
                time.sleep(0.8)

            #soup = BeautifulSoup(browser.page_source, 'lxml')
            soup = BeautifulSoup(browser.page_source, 'html.parser')
            all_downloadable_url += soup.find_all('img')

        browser.close()
        return self.allUrls(all_downloadable_url)


    def allUrls(self, images):
        urls = []
        for eachImage in images:
            if len(urls) == self.max_images :
                break
            data_src = eachImage.get('data-src')
            if data_src is not None and not data_src.find('https://'):
                urls.append(data_src)
            elif data_src is None:  # l'attribut data-src n'est pas dans la balise img
                src = eachImage.get('src')
                if not src.find('https://'):
                    urls.append(src)
        return urls