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

        self.searchUrl = 'https://www.google.fr/search?hl=fr&' \
                         'q='+ key_word + '&'\
                         'tbm=isch'

    def launchSearch(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        browser = webdriver.Chrome(self.webdriverUrl, options=options)
        browser.set_window_size(1280, 1024)
        browser.get(self.searchUrl)

        element = browser.find_element_by_tag_name('body')

        # Scroll down
        for i in range(27) :
            element.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.2)

        soup = BeautifulSoup(browser.page_source, 'lxml')

        images = soup.find_all('img')

        browser.close()

        return self.allUrls(images)


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