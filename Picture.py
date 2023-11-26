
import time
import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_img(img_link, name, index):
    if not os.path.isdir(name):
        os.mkdir(name)
    picture = requests.get(img_link)
    saver = open(os.path.join(f"{name}/{str(index).zfill(4)}.jpg"), "wb")
    saver.write(picture.content)
    saver.close()


def download_img(path, key) -> None:  

    os.chdir(path)
    if not os.path.isdir("dataset"):
        os.mkdir("dataset")
    os.chdir("dataset")

    count = 0
    page = 0
    
    while (count < 1000):
         
        key1=key.replace(" ", "%20")
        url = f"https://yandex.ru/images/search?p={page}&text={key1}"
        driver = webdriver.Chrome()
        driver.get(url = url)
        time.sleep(5)

        try:
            _ = driver.find_elements( By.CLASS_NAME, 'CheckboxCaptcha')
            input('Press enter after the captcha appears')
            driver.get(url = url)
            time.sleep(5)
        except Exception as e:
            print('Captcha missing')

        imgs = driver.find_elements( By.CLASS_NAME, 'SimpleImage-Image')
        print( imgs )



        for img in imgs:
           img_link = img.get_attribute('src') 
           get_img(img_link, key, count)
           count += 1
           print(img_link)
        page += 1
    driver.close()
    driver.quit()


def main():
    directory = os.getcwd()
    key = 'dogs'
    download_img(directory, key)
    
if __name__ == "__main__":
    main()

    