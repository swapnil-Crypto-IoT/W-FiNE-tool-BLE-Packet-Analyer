# Importing essential libraries
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests
# Set the driver path to chrome drive. It help to open website with
# chromium browser
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")


df = pd.read_csv("oui_ble_mac_upper.csv",sep=",")
f = open("image_http.txt","a")
for i in df.iloc[:,2]:
    url="https://www.google.com/search?q="+str(i)+" Company+logo"+"&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjkruuhlZPwAhV07HMBHX4DCXAQ_AUoAnoECAEQBA&biw=1294&bih=586"
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


    # # select src tag
    # image_src = [x['src'] for x in images]# select only jp format images
    # image_src = [x for x in image_src if x.endswith('.png')]
    # for image in image_src:
    #     print(image)
    
    
    # image_count = 1
    # for image in image_src:
    #     with open('image_'+str(image_count)+'.jpg', 'wb') as f:
    #         res = requests.get(image)
    #         f.write(res.content)
    #     image_count = image_count+1