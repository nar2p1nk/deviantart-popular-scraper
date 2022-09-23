from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
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

postDatas = soup2.find('div',class_='_1p-42 _6G8rT _39R1e')

numFavourites = postDatas.contents[0].contents[0].contents[0].contents[0].contents[0].contents[1]

numComments = postDatas.contents[0].contents[1].contents[0].contents[0].contents[0].contents[1].contents[0].contents[0]

numViews = postDatas.contents[0].contents[2].contents[0].contents[1].contents[0]


postCommentsParent =  soup2.find('div',class_='_1YhYy')

commentsList = postCommentsParent.contents[0].contents[1].contents[0].contents[0].contents[0].contents[0].contents

print(numComments,ws,len(commentsList),commentsList)



