from seleniumwire import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import json

def ReturnVideoLink(passed):
    shortcode = passed.replace("https://www.instagram.com/p/",'').replace('/','').replace("//",'')
    video = f"https://www.instagram.com/p/{shortcode}"
    chrome_options = Options()
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_argument("headless")
    chrome_options.add_argument("--autoplay-policy=no-user-gesture-required")
    svc = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=svc,chrome_options=chrome_options)
    driver.delete_all_cookies()
    driver.get(video)
    delay = 15
    soup = ''
    while(delay >= 0):
        try:
            soup = driver.execute_script("return document.querySelector('video').outerHTML;")
            break
        except Exception as e:
            print(e)
            time.sleep(1)
            delay -=1
    soup = BeautifulSoup(soup,'html.parser')
    soup = soup.findAll('video')
    video_link = soup[0]['src'].replace("&_nc_cat",'&amp:_nc_cat')
    return video_link
