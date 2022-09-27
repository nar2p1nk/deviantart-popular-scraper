from bs4 import BeautifulSoup
from selenium import webdriver
import string

ws = string.whitespace

url = 'https://www.deviantart.com/popular/deviations'

htmlClass = 'uU5En = deviantion title| MvjoN = user data| ._3_LJY = image|_121Hz'

#@PATH = r'/usercode.chomedriver'

#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver = webdriver.Firefox()

driver.get(url)


soup = BeautifulSoup(driver.page_source,'html.parser')

divCard = soup.find('section',class_='_3oBlM _2R889')

username = divCard.contents[1].contents[3].contents[1].contents[0].contents[1].contents[0].contents[0]['data-username']

userProfilePic = divCard.contents[1].contents[3].contents[1].contents[0].contents[1].contents[0].contents[0].contents[0]['src']

userProfileLink = divCard.contents[1].contents[3].contents[1].contents[0].contents[1].contents[0].contents[0]['href']

postTitle = divCard.contents[0]['aria-label']

postLink = divCard.contents[0]['href']

displayImage = divCard.contents[0].contents[0].contents[0]['src']

postImageSrcSet = divCard.contents[0].contents[0].contents[0]['srcset']

driver.get(postLink)

soup2 = BeautifulSoup(driver.page_source,'html.parser')

originalImage = soup2.find('img',class_='TZM0T _2NIJr')['src']


postNumbers = soup2.find('div',class_='_1p-42 _6G8rT _39R1e')

numFavourites = postNumbers.contents[0].contents[0].contents[0].contents[0].contents[0].contents[1]

numComments = postNumbers.contents[0].contents[1].contents[0].contents[0].contents[0].contents[1].contents[0].contents[0]

numViews = postNumbers.contents[0].contents[2].contents[0].contents[1].contents[0]

timePosted = soup2.find('span',class_='_12Yqs _1lf7Q')





