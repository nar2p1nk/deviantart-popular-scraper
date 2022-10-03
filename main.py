from bs4 import BeautifulSoup
from selenium import webdriver
import string
import requests
import shutil
import model
import os 


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
    
    numFavourites = postNumbers.contents[0].contents[0].contents[0].contents[0].contents[0].contents[1].contents[0].contents[0]
    
    numFavourites = numFavourites[:len(numFavourites) - 1] +'000' if numFavourites[-1] == 'K' else numFavourites

    numComments = postNumbers.contents[0].contents[1].contents[0].contents[0].contents[0].contents[1].contents[0].contents[0]

    numComments = numComments[:len(numComments) - 1] + '000' if numComments[-1] == 'K' else numComments
    
    numViews = postNumbers.contents[0].contents[2].contents[0].contents[1].contents[0].contents[0]

    numViews = numViews[:len(numViews) -1 ] + '000' if numViews[-1] == 'K' else numViews

    timePosted = soup2.find('span',class_='_12Yqs _1lf7Q').contents[1]
    
    datetimePosted = timePosted['datetime'][0:10] + ' ' + timePosted['datetime'][11:19]
    
    timePostedTitleUTC = timePosted['aria-label']
    
    timePostedTitleGmt =  timePosted['title']

    r = requests.get(displayImage,stream=True)

    re = requests.get(originalImage,stream=True)

    rex = requests.get(userProfileLink,stream=True)

    if r.status_code and re.status_code == 200:

        r.raw.decode_content = True

        re.raw.decode_content = True

        filename = postTitle.replace(' ','_').lower()


        if model.OtherUser.get_or_none(username=username):
            print('user: '+username+' already exist')
            pass
        else:
            True
            with open('./images/profilePictures/'+username,'wb') as f:
                shutil.copyfileobj(re.raw,f)

            print('profile picture: '+username+'. downloaded')
            user = model.OtherUser(username=username,profilePicture=os.path.abspath('images/profilePictures/'+username))
            user.save()
            print('user: '+username+'. saved')


        if model.OtherPost.get_or_none(postTitle=postTitle):
            print('post: '+postTitle+' already exist')
            False
        else:
            True
            with open('./images/display/'+filename,'wb') as f:
                shutil.copyfileobj(r.raw,f)

                print('display file: '+filename+'. downloaded')

            with open('./images/original/'+filename,'wb') as f:
                shutil.copyfileobj(re.raw,f)

                print('original file: '+filename+'. downloaded')

            post = model.OtherPost(postTitle=postTitle,displayImageLink=os.path.abspath('images/display/'+filename),
                                   originalImageLink = os.path.abspath('images/original/'+filename),
                                   numFavourites=numFavourites,numViews=numViews,numComments=numComments,PostedBy=username,timePosted=datetimePosted)
            post.save()
            print('post: '+postTitle+'. saved')

    else:
        print('err')

    num += 1
    print(num)






