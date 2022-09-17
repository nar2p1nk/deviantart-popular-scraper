
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import sqlite3

url = 'https://www.deviantart.com/popular/deviations'

htmlClass = 'uU5En = deviantion title| MvjoN = user data| ._3_LJY = image|_121Hz'

#@PATH = r'/usercode.chomedriver'

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get(url)


soup = BeautifulSoup(driver.page_source,'html.parser')

responseImages = soup.find_all('div',class_='_3_LJY')

responseTitle = soup.find_all('h2',class_='_3CpJS')

responseUsername = soup.find_all('span',class_='_2EfV7')

responseUserProfile = soup.find_all('img',class_='_121Hz')

responseUserLink = soup.find_all('a',class_='user-link')

#responseTitleAndUserData = soup.find_all('div',class_='_34lVt')

data = []

y = 0


con = sqlite3.connect('deviantart.db')

cur = con.cursor()

cur.execute('''create TABLE IF NOT EXISTS posts(
title TEXT NOT NULL,
images TEXT NOT NULL,
username TEXT NOT NULL,
userProfilePicture TEXT NOT NULL,
userProfileLink TEXT NOT NULL
            )''')

for x in responseTitle:

    parse = {
        'title':x.get_text(),
        'images':responseImages[y].img['src'],
        'username':responseUsername[y].get_text(),
        'user profile':responseUserProfile[y]['src'],
        'user profile link':'https://www.deviantart.com/' + responseUsername[y].get_text()
    }

    cur.execute('''INSERT INTO posts) VALUES(%s,%s,%s,%s,https://www.deviantart.com/%s)'''% (x.get_text(),responseImages[y].img['src'],responseUsername[y].get_text(),responseUserProfile[y]['src'],responseUsername[y].get_text()))

    print(parse)

    data.append(parse)

    y += 1




