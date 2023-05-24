#importing libraries
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# initialize the chrome driver
driver=webdriver.Chrome(ChromeDriverManager().install())

# webiste URL
website = "https://www.google.com/search?q=site%3Ayoutube.com+openinapp.co&rlz=1C5CHFA_enIN1027IN1029&oq=site%3Ayoutube.com+openinapp.co&aqs=chrome..69i57j69i58.2486314j0j7&sourceid=chrome&ie=UTF-8"

# open the website in chrome with required search
driver.get(website)
# maximize the window
driver.maximize_window()
# finding button to go for next page of google search
button =driver.find_element(By.CSS_SELECTOR,'div#botstuff td.d6cvqb.BBwThe')
# create a list to store all the links
Alllinks=[]
#running loop until the length of Alllinks list become 10000 for first 10000 links
while(len(Alllinks)<=10000):
    #selecting the elements to get link.
    link1=driver.find_elements(By.CSS_SELECTOR,'div.yuRUbf a')
    #As their are two type of links which is used by google for search I am getting both type of links of the page.
    link2=driver.find_elements(By.CSS_SELECTOR,'div.DhN8Cf a')
    # traversing the list of links in link1 and append in Alllinks list.
    for i in link1:
        Alllinks.append(i.get_attribute("href"))
        # checking the length of alllinks
        if(len(Alllinks)==10000):
            break
    # checking the length of alllinks
    if (len(Alllinks) == 10000):
        break
    # traversing link2 and appending it in same list Alllinks
    for i in link2:
        Alllinks.append(i.get_attribute("href"))
        # checking the length of alllinks
        if(len(Alllinks)==10000):
            break
    # now all the links of the page is stored in the list so click on the button to goto the next page.
    button.click()
# saving the list in the form of csv by using pandas
# creating dictionary to convert easily in csv using pandas
dic ={'Youtube_Links' : Alllinks}
#creating dataframe from dictionary
df =pd.DataFrame.from_dict(dic)
#saving dataframe as csv file by name youtube_links
df.to_csv("youtube_links",index=False)