from bs4 import BeautifulSoup
from selenium import webdriver
import string
import requests
import shutil

ws = string.whitespace

url = 'https://www.deviantart.com/popular/deviations'

htmlClass = 'uU5En = deviantion title| MvjoN = user data| ._3_LJY = image|_121Hz'

#@PATH = r'/usercode.chomedriver'

#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver = webdriver.Firefox()

driver.get(url)


soup = BeautifulSoup(driver.page_source,'html.parser')

divCards = soup.findAll('section',class_='_3oBlM _2R889')

num = 0

for divCard in divCards:

    username = divCard.contents[1].contents[3].contents[1].contents[0].contents[1].contents[0].contents[0]['data-username']
    
    userProfilePic = divCard.contents[1].contents[3].contents[1].contents[0].contents[1].contents[0].contents[0].contents[0]['src']
    
    userProfileLink = divCard.contents[1].contents[3].contents[1].contents[0].contents[1].contents[0].contents[0]['href']
    
    postTitle = divCard.contents[0]['aria-label']
    
    postLink = divCard.contents[0]['href']
    
    displayImage = divCard.contents[0].contents[0].contents[0]['src']
    
#    postImageSrcSet = divCard.contents[0].contents[0].contents[0]['srcset']
    
    driver.get(postLink)
    
    soup2 = BeautifulSoup(driver.page_source,'html.parser')
    
    originalImage = soup2.find('img',class_='TZM0T _2NIJr')['src']
    #_1O2S9 _19exo
    
    postNumbers = soup2.find('div',class_='_1p-42 _6G8rT _39R1e')
    
    numFavourites = postNumbers.contents[0].contents[0].contents[0].contents[0].contents[0].contents[1]
    
    numComments = postNumbers.contents[0].contents[1].contents[0].contents[0].contents[0].contents[1].contents[0].contents[0]
    
    numViews = postNumbers.contents[0].contents[2].contents[0].contents[1].contents[0]
    
    timePosted = soup2.find('span',class_='_12Yqs _1lf7Q').contents[1]
    
    datetimePosted = timePosted['datetime'][0:10] + ' ' + timePosted['datetime'][11:19]
    
    timePostedTitleUTC = timePosted['aria-label']
    
    timePostedTitleGmt =  timePosted['title']


    r = requests.get(displayImage,stream=True)

    re = requests.get(originalImage,stream=True)

    if r.status_code and re.status_code == 200:

        r.raw.decode_content = True

        re.raw.decode_content = True

        displayFilename = 'display ' + postTitle

        originalFilename = 'original ' + postTitle

        with open('./images/display/'+postTitle.replace(' ','_').lower(),'wb') as f:
            shutil.copyfileobj(r.raw,f)

            print('display file: '+postTitle+'. downloaded')

        with open('./images/original/'+postTitle.replace(' ','_').lower(),'wb') as f:
            shutil.copyfileobj(re.raw,f)

            print('original file: '+postTitle+'. downloaded')

    else:
        print('err')

    num += 1
    print(num)






