# Importing essential libraries
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests
import urllib.request
from bing_image_downloader import downloader
import os
# Set the driver path to chrome drive. It help to open website with
# chromium browser
# driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")


df = pd.read_csv("oui_ble_mac_upper.csv",sep=",")
f = open("image_http_5.txt","r")
lines = f.readlines()
os.mkdir("image_http_5")
os.chdir("image_http_5")
for i,line in enumerate(lines,14912):
    try:
           url = line
           if "jpg" in line:
               urllib.request.urlretrieve(str(url),str(df.iloc[i,2])+".jpg")
           else:
               urllib.request.urlretrieve(str(url),str(df.iloc[i,2])+".png")
    except FileNotFoundError:
        pass
            
                   
               

    # for i in df.iloc[0:3728,2]:
    #     url="https://www.google.com/search?q="+str(i)+" Company+logo"+"&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjkruuhlZPwAhV07HMBHX4DCXAQ_AUoAnoECAEQBA&biw=1294&bih=586"
    #     driver.get(url)
    #     # read the page source i.e. html code 
    #     content = driver.page_source 
    #     soup = BeautifulSoup(content,features="html.parser")
        
    #     i = soup.findAll('img',src=True,attrs={'class':'rg_i Q4LuWd'})
    #     c=0
    #     # print(i)
    #     for count,image in enumerate(i):
    #         if(count<1):
                
    #             f.write("{}\n".format(image['src']))
    #             print(count)
        
    # f.close()
