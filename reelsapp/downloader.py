from seleniumwire import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import json
import re
from urllib.parse import urlparse, urlunparse

def ReturnVideoLink(passed):
    shortcode = ''
    if "reel" in passed or "reels" in passed:
        shortcode = re.findall(r"/(reel[s]?)/([A-Za-z0-9_-]+)", passed)[0][1]
    elif "p" in passed:
        shortcode = re.findall(r"/p/([A-Za-z0-9_-]+)", passed)[0]
    else:
        return None  
    
    video = f"https://www.instagram.com/p/{shortcode}"
    
    parsed_url = urlparse(video)
    clean_url = urlunparse(parsed_url._replace(query=''))
    
    chrome_options = Options()
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_argument("headless")
    chrome_options.add_argument("--autoplay-policy=no-user-gesture-required")
    svc = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=svc, chrome_options=chrome_options)
    driver.delete_all_cookies()
    driver.get(clean_url)
    delay = 15
    soup = ''
    while delay >= 0:
        try:
            soup = driver.execute_script("return document.querySelector('video').outerHTML;")
            break
        except Exception as e:
            print(e)
            time.sleep(1)
            delay -= 1
            print("Sonu")
    soup = BeautifulSoup(soup, 'html.parser')
    soup = soup.findAll('video')
    video_link = soup[0]['src'].replace("&_nc_cat", "&amp:_nc_cat")
    return video_link
