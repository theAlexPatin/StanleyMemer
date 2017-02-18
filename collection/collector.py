__author__ = 'apatin'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import json
import urllib
import os
import threading
path_to_chromedriver = '/usr/local/bin/chromedriver'    ####Change path!

sQuery = ''



def scroll(driver):
    driver.implicitly_wait(100)
    scheight = .1
    while scheight < 9.9:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight/%s);" % scheight)
        scheight += .01

def downloadImage(imgUrl):
    filename = imgUrl.split('/')[-1]	#Gets the name of the image
    try:
        path = 'images'
        if 'memes' in sQuery:
            print('memes')
            path = 'memes'
        if not os.path.exists(path):
            os.makedirs(path)
        path = path +'/'+ filename
        urllib.request.urlretrieve(imgUrl, path)
    except:
        print('error downloading')

def findImages(driver):
    source = driver.page_source		#Gets the source of the page
    soup = BeautifulSoup(source, 'html')	#Parses the source
    driver.close()	
    threads = []
    try:
        for data in soup.find_all('div', attrs={'class': 'rg_meta'}):		#Finds all "a" tags with the "rg_l" class
            data = json.loads(data.string)
            url = data['ou']
            t = threading.Thread(target=downloadImage, args=(url,))
            t.start()
            threads.append(t)
    except:
        print("There were no images available")

    for t in threads:
        t.join()

def main():
    driver = webdriver.Chrome(executable_path = path_to_chromedriver)
    driver.get("https://www.google.com/images")
    elem = driver.find_element_by_id("lst-ib")	#Finds the search box (has this id tag)
    elem.send_keys(sQuery)
    elem.send_keys(Keys.RETURN)
    scroll(driver)	#Dynamically loads images
    findImages(driver)


if __name__ == "__main__":
    sQuery = input("Please enter search query: ")
    main()