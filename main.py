from bs4 import BeautifulSoup
from selenium import webdriver
import string
import requests
import shutil
import model
import os 
ws = string.whitespace

url = 'https://www.deviantart.com/topic/street-art'

driver = webdriver.Firefox()

driver.get(url)


soup = BeautifulSoup(driver.page_source,'html.parser')

divCards = soup.findAll('section',class_='_3oBlM _2R889')

num = 0

for divCard in divCards:


    try:
        postLink = divCard.contents[0]['href']
    

        displayImage = divCard.contents[0].contents[0].contents[0]['src']
 
       
        driver.get(postLink)


    except:
        pass
   
    

    soup2 = BeautifulSoup(driver.page_source,'html.parser')

    username = soup2.find('span',class_='_12F3u').contents[0]

    postTitle = soup2.find('h1',attrs={'data-hook':'deviation_title'}).contents[0]

    originalImage = soup2.find('img',alt=postTitle)['src']
    
    userProfilePic = soup2.find('img',alt=username+'\'s avatar')['src']

    numFavourites = soup2.find('span',attrs={'data-hook':'faves_counter'}).contents[0].contents[0].contents[1].contents
    
    numFavourites = numFavourites[:len(numFavourites) - 1] +'000' if numFavourites[-1] == 'K' else numFavourites

    numComments = soup2.find('div',attrs={'data-hook':'comments_count'}).contents[1].contents[0]

    numViews = soup2.find('div',class_='_1p-42 _6G8rT _39R1e').contents[0].contents[2].contents[0].contents[1].contents[0].contents[0]

    numViews = numViews[:len(numViews) -1 ] + '000' if numViews[-1] == 'K' else numViews

    timePosted = soup2.find('span',class_='_12Yqs _1lf7Q').contents[1]
    
    datetimePosted = timePosted['datetime'][0:10] + ' ' + timePosted['datetime'][11:19]
    
    timePostedTitleUTC = timePosted['aria-label']
    
    timePostedTitleGmt =  timePosted['title']

    r = requests.get(displayImage,stream=True)

    re = requests.get(originalImage,stream=True)

    rex = requests.get(userProfilePic,stream=True)

    if r.status_code and re.status_code == 200:

        r.raw.decode_content = True

        re.raw.decode_content = True


        filename = postTitle.replace(' ','_').lower()


        if model.OtherUser.get_or_none(username=username):
            print('user: '+username+' already exist')
            pass
        else:
            if os.path.exists('images/profilePictures/'+username) == False:
                with open('./images/profilePictures/'+username,'wb') as f:
                    shutil.copyfileobj(rex.raw,f)
                    print('profile picture: '+username+'. downloaded')
            else:
                print('profile picture for user: '+username+' already exist')

            user = model.OtherUser(username=username,profilePicture='images/profilePictures/'+username)
            user.save()
            print('user: '+username+'. saved')


        if model.OtherPost.get_or_none(postTitle=postTitle):
            print('post: '+postTitle+' already exist')
            pass
        else:
            userquery = model.OtherUser.get(model.OtherUser.username == username)

            post = model.OtherPost(postTitle=postTitle,displayImageLink='images/display/Display_'+filename,
                                       originalImageLink ='images/original/Original_'+filename,numFavourites=numFavourites,numViews=numViews,
                                       numComments=numComments,PostedBy=userquery.otherId,timePosted=datetimePosted)
            post.save()
            print('post: '+postTitle+'. saved')

        if os.path.exists('images/display/Display_'+filename) == False:
            with open('./images/display/Display_'+filename,'wb') as f:
                shutil.copyfileobj(r.raw,f)

                print('display file: '+postTitle+'. downloaded')
        else:
            print('display image: '+postTitle+' already exist')
            pass

        if os.path.exists('images/original/Original_'+filename) == False:
            with open('./images/original/Original_'+filename,'wb') as f:
                shutil.copyfileobj(re.raw,f)
            
                print('original file: '+filename+'. downloaded')

        else:
            print('original image: '+filename+' already exist')
            pass
                
#                userquery = model.OtherUser.get(model.OtherUser.username == username)

#                post = model.OtherPost(postTitle=postTitle,displayImageLink='images/display/'+filename,
#                                      originalImageLink ='images/original/'+filename,numFavourites=numFavourites,numViews=numViews,
#                                       numComments=numComments,PostedBy=userquery.otherId,timePosted=datetimePosted)
#                post.save()
#                print('post: '+postTitle+'. saved')

    else:
        print('err')

    num += 1
    print(num)






