#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 16:38:46 2021

@author: swapnil
"""


# Objective : Run the various python script parallel. Moreover, this code
# runs the multiple file which will download the different company url from 
# website into a folder. 

# import essential libraries
import os
from multiprocessing import Pool


# create a list that holds python script to run parallel
process_list = ["web_scraping_OUILOGOs_4.py","web_scraping_OUILOGOs_8.py"]
# for i in range(0,8):
#     print("web_scraping_OUILOGOs_{}.py".format(i+1))
#     process_list.append("web_scraping_OUILOGOs_{}.py".format(i+1))

# convert list to tuple
process = tuple(process_list)

# define a function that execute a process into sytem using python
def run_process(task):
    
    os.system('python3 {}'.format(task))

# parallelizing the process using pool library function
# assigned the number of process assigned in the tuple 
pool = Pool(2)
# call run_process function using pool which make all the process parallel
pool.map(run_process,process)
print("Completed..!") 
    

