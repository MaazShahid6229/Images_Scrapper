# import libraries
import os
import io
import time
import json
import requests
import selenium
from PIL import Image
from selenium import webdriver
from urlextract import URLExtract
from selenium.webdriver.common.by import By
from webdrivermanager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException

# setting chrome extesion
chrome_driver_path = r"C:\Users\Maaz\Desktop\Images_Bot\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.maximize_window()


# open url json
filename = "url.json"
f = open(filename)
urls = json.load(f)


def get_image(url):
    mypath = f"C:/Users/Maaz/Desktop/Images_Bot/{url[-6:-1]}"
    if not os.path.isdir(mypath):
        os.makedirs(mypath)
    driver.get(url)
    time.sleep(2)
    image1 = driver.find_element(By.CLASS_NAME, "sm-tile")
    image1.click()

    while True:
        try:
            time.sleep(2)
            main_img = driver.find_element(By.CLASS_NAME, "sm-lightbox-v2-photo")
            img_style = main_img.get_attribute("style")
            img_name = main_img.get_attribute("alt")
            extractor = URLExtract()
            img_urls = extractor.find_urls(img_style)
            print(img_urls[0])
            img_data = requests.get(img_urls[0]).content
            with open(f'{mypath}/{img_name}', 'wb') as handler:
                handler.write(img_data)
            time.sleep(1)
            next_img = driver.find_element(By.CSS_SELECTOR, "body > div.sm-user-ui.sm-user-overlay-container > div > div > div > div > button:nth-child(5)")
            next_img.click()
        except:
            break


for url in urls["url"]:
    get_image(url)


