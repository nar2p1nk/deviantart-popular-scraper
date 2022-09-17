
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import string
url = 'https://www.deviantart.com/popular/deviations'

htmlClass = 'uU5En = deviantion title| MvjoN = user data| ._3_LJY = image|_121Hz'

#@PATH = r'/usercode.chomedriver'

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get(url)


soup = BeautifulSoup(driver.page_source,'html.parser')

divCard = soup.find('section',class_='_3oBlM _2R889')

#postTitle = divCard.contents[0]['aria-label']

#postLink = divCard.contents[0]['href']

#postImage = divCard.contents[0].contents[0].contents[0]['src']

#postImageSrcSet = divCard.contents[0].contents[0].contents[0]['srcset']

print(divCard)

print(string.whitespace,divCard.contents[0])

print(string.whitespace,divCard.contents[1])

