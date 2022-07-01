# Importing essential libraries
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests
import time
# Set the driver path to chrome drive. It help to open website with
# chromium browser
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

df = pd.read_csv("oui_ble_mac_upper.csv",sep=",")
f = open("image_http_3.txt","a")
for i in df.iloc[7456:11184,2]:
    url="https://www.google.com/search?q="+str(i)+" Company+logo"+"&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjkruuhlZPwAhV07HMBHX4DCXAQ_AUoAnoECAEQBA&biw=1294&bih=586"
    time.sleep(1)
    driver.get(url)
    # read the page source i.e. html code 
    content = driver.page_source 
    soup = BeautifulSoup(content,features="html.parser")
    
    i = soup.findAll('img',src=True,attrs={'class':'rg_i Q4LuWd'})
    c=0
    # print(i)
    for count,image in enumerate(i):
        if(count<1):
            
            f.write("{}\n".format(image['src']))
            print(count)
    
f.close()
