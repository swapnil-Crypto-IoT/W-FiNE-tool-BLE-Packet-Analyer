#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 10:58:33 2021

@author: swapnil
"""

# Importing essential libraries
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests
# Set the driver path to chrome drive. It help to open website with
# chromium browser
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

url="http://domoticx.com/bluetooth-class-of-device-lijst-cod/"
driver.get(url)
# read the page source i.e. html code 
content = driver.page_source 
soup = BeautifulSoup(content,features="lxml") 

dfs = pd.read_html(content)

# f = open("CoD_database.csv",'a')
# counter=0
# for i in dfs:
#     counter+=1
#     i.to_csv('data_'+str(counter)+'.csv')