#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 11:16:20 2021

@author: swapnil
"""


# objective: Developed a tool using tkinter which extract the 
#            details of the BLE/Bluetooth based IoT node

# This code extract all the details of IoT node which suports only 
# BLE application. Details are extracted with the help of Class of 
# of devices and other UUIDs

# importing tkinter library for GUI 
import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import pandas as pd
import glob,os

# importing user defined py library to import 16/128 bit uuids values
from uuid16 import * 
from CoD_hex import *
from oui_ble_mac_upper import *

# User define function
def selection():  
   selection =  ""+(radio.get()) +" is selected !"  
   selection_msg.config(text = selection)

# User defined function to extract details based on CoD
def cod_based_extraction():
    df=pd.read_csv('cod_database_updated.csv',sep=',')
    frame2_top1.delete(1.0,END)
    value = (CoD_hex_chosen.get())
    print(value)
    c=0
    for i in df.iloc[:,1]:
        
        if(i==value):
            # data=df.iloc[c,2:6].values
            
            frame2_top1.insert(1.0,("\n\nCoD Binary:-- \n"+str(df.iloc[c,2])+"\n\nCoD bits details: --\n"+str(df.iloc[c,3])+"\n\nPossible Devices:-- \n"+str(df.iloc[c,4])+"\n\nProbable Address:--\n"+str(df.iloc[c,5])))
            frame2_top1.config(font = ("MS Mincho", 13,"bold"),fg="midnight blue")
        c+=1
# user defined function to extract details based on uuid16
def uuid_16_based_extraction():
    df1=pd.read_csv('16_bit_uuid_database_1.csv',sep=',')
    frame3.config(text = None)
    value= uuid16bit_chosen.get()
    c=0
    for i in df1.iloc[:,1]:
        # print(i)
        if (i==value):
            print("{}-{}".format(i,str(df1.iloc[c,2])))
            # frame3.insert(1.0,(str(df1.iloc[c,2])))
            frame3.config(text=(str(df1.iloc[c,2])),font = ("MS Mincho", 13,"bold"),fg="white",anchor=CENTER,wraplength=200)
        c+=1

# user defined function to extract details based on uuid16
def uuid_128_based_extraction():
    df2=pd.read_csv('128_bit_uuid_database.csv',sep=',')
    frame4.config(text=None)
    value = uuid128bit_chosen.get()
    c=0
    for i in df2.iloc[:,0]:
        if (i==value):
            print(value)
            # foldername= "/Product/"+str(df2.iloc[c,1]+"/*.png")
            tmp = "Product/"+str(df2.iloc[c,1])+"/"
            # os.chdir(tmp)
            for file_1 in glob.glob(tmp+"*.png"):
                print(tmp)
                print(str(file_1))
            # file_png= glob.glob(tmp)
                img = Image.open(file_1)
                # img.show()
                img1 = img.resize((150, 150))
                # img.show()
                img1 = ImageTk.PhotoImage(img1)
                
                frame4.config(image=img1)
                frame4.image=img1
                
        # os.chdir("")
        c+=1
# user defined function to identify BLE company using OUI
df3=pd.read_csv('oui_ble_mac_upper.csv',sep=',')
def oui_mac_id_based_extraction():
    df3=pd.read_csv('oui_ble_mac_upper.csv',sep=',')
    frame2_bottom.config(text=None)
    value = oui_mac_id_chosen.get()
    c=0
    for i in df3.iloc[:,1]:
        if (i==value):
            print(df3.iloc[c,2])
            frame2_bottom.config(text=(str(df3.iloc[c,2])),font = ("MS Mincho", 13,"bold"),fg="blue",anchor=CENTER,wraplength=200)
            # downloaded company logo insertion in frame 
            tmp = "parallel_python3_code_for_image_scraping/Image_download_from_copiedurls/all_images/"+str(df3.iloc[c,2])+".png"
            print(tmp)
            
            img = Image.open(tmp)
            # img.show()
            img1 = img.resize((300, 150))
            # img.show()
            img1 = ImageTk.PhotoImage(img1)
            
            frame4.config(image=img1)
            frame4.image=img1
        c+=1

# defined main windows
root = tk.Tk(screenName=None, baseName="Device Analyser", className= " IoT Node Analyser ", useTk=1)
root.geometry("1500x700")
root.iconphoto(False, tk.PhotoImage(file='lelogo.png'))
# (label)logic for background image in GUI 
background_image = tk.PhotoImage(file='back_ground.png')
background_label = tk.Label(root, image = background_image, width="1500", height="700")
background_label.place(relx=0, rely =0, relwidth=1, relheight=1)

# Creat a frame for manufacture name and other BLE details
frame_base2 = tk.Frame(root,bg = "midnightblue", width = "615", height = "350")
frame_base2.place(relx=0.025, rely=0.45)
frame_2 = tk.Label(frame_base2)
frame_2.place(relx=0.01,rely=0.01,relwidth = 0.98, relheight=0.98)
labelframe = tk.LabelFrame(frame_2,font=("Helvetica","12","bold"), text="CoD data extraction",bg="midnight blue",fg="white",labelanchor = 'n')
labelframe.pack(fill="both", expand="yes")
frame2_top1 = tk.Text(labelframe,bg = "light sky blue",wrap=tk.WORD)
frame2_top1.place(relx=0.01, rely=0.04, relwidth =0.98, relheight = 0.6)
# creat and add a scrollbar to lower_frame
scrollbar = tk.Scrollbar(frame2_top1,  command=frame2_top1.yview, orient='vertical')
scrollbar.pack(side=RIGHT, fill = Y )
frame2_top1.config(yscrollcommand=scrollbar.set)
# create lable widget for OUI company IDs
labelframe_cod = tk.LabelFrame(frame_2,font=("Helvetica","12","bold"), text="OUI-MAC based Company Identification",bg="midnight blue",fg="white",labelanchor = 'n')
labelframe_cod.place(relx=0.01, rely=0.66, relwidth =0.98, relheight = 0.32)
# labelframe_cod.pack(fill="both", expand="yes")
frame2_bottom = tk.Label(labelframe_cod,bg = "light sky blue")
frame2_bottom.place(relx=0.01, rely=0.01, relwidth =0.98, relheight = 0.92)

#  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Creat a frame for button elements such as class, UUID-16, UUID-18
frame1 = tk.Frame(root,bg = "#364F6B", width = "1230", height = "250")
frame1.place(relx=0.025, rely=0.05)
list_1 = (cod_hex_values)
CoD_hex_chosen = ttk.Combobox(frame1, values=list_1) 
CoD_hex_chosen.config(font = ("Courier", "12", "bold"), justify = CENTER, state=DISABLED)
CoD_hex_chosen.current(0)
CoD_hex_chosen.set('--Select BLE CoD (Class of Device)--')
CoD_hex_chosen.place(relx=0.23, rely=0.1, relwidth = 0.35, relheight = 0.12)
photo5 = PhotoImage(file = "iconfinder_search_1608826.png")
codsearch=tk.Button(frame1, command = cod_based_extraction)
pic5 = photo5.subsample(30,30)
codsearch.config(image = pic5, compound = RIGHT,state=DISABLED)
codsearch.place( relx = 0.58 , rely = 0.1 , relwidth = 0.05 , relheight = 0.12 )



# Displaying logo of BLE application as bluetooth analyser
load = Image.open("blelogodesign.png")
load = load.resize((300,150),Image.ANTIALIAS)
render = ImageTk.PhotoImage(load)
img = Label(frame1, image=render,bg="#364F6B")
img.image = render
img.place(relx = 0.71, rely = 0.05, x=0, y=0)


radio = StringVar()
# Radio button 1 setting: CoD selection and pop up menu for all CoD
radio_but1 = tk.Radiobutton(frame1,text="Class Identifiers", bg="#364F6B",fg="gold", font = ("Times new roman", "12", "bold"),value="CoD based mapping", variable=radio, command=lambda:[selection()])
radio_but1.place(relx=0.025, rely=0.1)

 
radio_but2 = tk.Radiobutton(frame1,text="16-bit UUIDs", bg="#364F6B",fg="gold", font = ("Times new roman", "12", "bold"),value="16-bit UUID based mapping", variable=radio, command=selection)
radio_but2.place(relx=0.025, rely=0.3)
list_2 = (uuid_16values)
uuid16bit_chosen = ttk.Combobox(frame1, values=list_2)
uuid16bit_chosen.config(font = ("Courier", "12", "bold"), justify = CENTER, state=DISABLED)
uuid16bit_chosen.current(0)
uuid16bit_chosen.set('-- 16-bit UUID --')
uuid16bit_chosen.place(relx=0.23, rely=0.3, relwidth = 0.35, relheight = 0.12)
uuid16search=tk.Button(frame1, command = uuid_16_based_extraction)
uuid16search.config(image = pic5, compound = RIGHT,state=DISABLED)
uuid16search.place( relx = 0.58 , rely = 0.3 , relwidth = 0.05 , relheight = 0.12 )



radio_but3 = tk.Radiobutton(frame1,text="128-bit UUID", bg="#364F6B",fg="gold", font = ("Times new roman", "12", "bold"),value="128-bit UUID based mapping", variable=radio, command=selection)
radio_but3.place(relx=0.025, rely=0.5)
list_3=(uuid128_values)
uuid128bit_chosen = ttk.Combobox(frame1, values=list_3)
uuid128bit_chosen.config(font = ("Courier", "12", "bold"), justify = CENTER, state=DISABLED)
uuid128bit_chosen.current(0)
uuid128bit_chosen.set('-- 128-bit UUID --')
uuid128bit_chosen.place(relx=0.23, rely=0.5, relwidth = 0.35, relheight = 0.12)
uuid128search=tk.Button(frame1, command = uuid_128_based_extraction)
uuid128search.config(image = pic5, compound = RIGHT,state=DISABLED)
uuid128search.place( relx = 0.58 , rely = 0.5 , relwidth = 0.05 , relheight = 0.12 )


radio_but4 = tk.Radiobutton(frame1,text="OUI MAC ID", bg="#364F6B",fg="gold", font = ("Times new roman", "12", "bold"),value="OUI MAC based Company Identification", variable=radio, command=selection)
radio_but4.place(relx=0.025, rely=0.7)
list_4=(oui_mac_id)
oui_mac_id_chosen = ttk.Combobox(frame1, values=list_4)
oui_mac_id_chosen.config(font = ("Courier", "12", "bold"), justify = CENTER, state=DISABLED)
oui_mac_id_chosen.current(0)
oui_mac_id_chosen.set('-- OUI MAC UPPER (UAP)--')
oui_mac_id_chosen.place(relx=0.23, rely=0.7, relwidth = 0.35, relheight = 0.12)
oui_mac_idsearch=tk.Button(frame1, command = oui_mac_id_based_extraction)
oui_mac_idsearch.config(image = pic5, compound = RIGHT,state=DISABLED)
oui_mac_idsearch.place( relx = 0.58 , rely = 0.7 , relwidth = 0.05 , relheight = 0.12 )




selection_msg = tk.Label(frame1,bg="#364F6B",fg="white",font = ("Times", "14", "bold"),justify=CENTER,wraplength=260)  
selection_msg.place(relx = 0.705,rely=0.66,relwidth = 0.25, relheight = 0.21)  
#  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


# Creat a frame for images to be displayed for manufacture (Company logo)
framebase3 = tk.Frame(root,bg = "light sky blue", width = "550", height = "350")
framebase3.place(relx=0.54, rely=0.45)
# keep label on framebase to insert labelframe
frame_3 = tk.Label(framebase3,width = "615", height = "300")
frame_3.place(relx=0.01, rely=0.02, relwidth =0.98, relheight = 0.35)
# keep labelframe on root based framebase3 variable
labelframe = tk.LabelFrame(frame_3,font=("Times","12","bold"), text="16-bit UUID based Company Identification",bg="midnight blue",fg="white",labelanchor = 'n')
labelframe.pack(fill="both", expand="yes")
# Now, keep frame3 label to display company name on button using uuid 16
frame3 = tk.Label(labelframe,bg = "midnight blue")
frame3.place(relx=0.1, rely=0.1, relwidth =0.8, relheight = 0.8)

# create a frame_4 label for labelframe 128 bit uuid image
frame_4 = tk.Label(framebase3,width = "615", height = "150")
frame_4.place(relx=0.01, rely=0.38, relwidth =0.98, relheight = 0.6)
# keep labelframe on root based framebase3 variable
labelframe = tk.LabelFrame(frame_4,font=("Times","12","bold"), text="Company logo (128-bit UUID/ OUI-mac-ID)",bg="midnight blue",fg="white",labelanchor = 'n')
labelframe.pack(fill="both", expand="yes")
frame4 = tk.Label(labelframe,bg = "white")
frame4.place(relx=0.1, rely=0.1, relwidth =0.8, relheight = 0.8)

# Radio button configuration setting logic
radio_but1.config(command = lambda: [selection(),
                                     uuid16bit_chosen.config(state=DISABLED),
                                     uuid128bit_chosen.config(state=DISABLED),
                                     CoD_hex_chosen.config(state=ACTIVE),
                                     codsearch.config(state=ACTIVE),
                                     uuid128search.config(state=DISABLED),
                                     uuid16search.config(state=DISABLED),
                                     oui_mac_id_chosen.config(state=DISABLED),
                                     oui_mac_idsearch.config(state=DISABLED)
                                     ])
radio_but2.config(command = lambda: [selection(),
                                     uuid16bit_chosen.config(state=ACTIVE),
                                     uuid128bit_chosen.config(state=DISABLED),
                                     CoD_hex_chosen.config(state=DISABLED),
                                     uuid128search.config(state=DISABLED),
                                     uuid16search.config(state=ACTIVE),
                                     oui_mac_id_chosen.config(state=DISABLED),
                                     oui_mac_idsearch.config(state=DISABLED)
                                     ])
radio_but3.config(command = lambda: [selection(),
                                     uuid16bit_chosen.config(state=DISABLED),
                                     uuid128bit_chosen.config(state=ACTIVE),
                                     CoD_hex_chosen.config(state=DISABLED),
                                     uuid128search.config(state=ACTIVE),
                                     uuid16search.config(state=DISABLED),
                                     oui_mac_id_chosen.config(state=DISABLED),
                                     oui_mac_idsearch.config(state=DISABLED)
                                     ])
radio_but4.config(command = lambda: [selection(),
                                     uuid16bit_chosen.config(state=DISABLED),
                                     uuid128bit_chosen.config(state=DISABLED),
                                     CoD_hex_chosen.config(state=DISABLED),
                                     uuid128search.config(state=DISABLED),
                                     uuid16search.config(state=DISABLED),
                                     oui_mac_id_chosen.config(state=ACTIVE),
                                     oui_mac_idsearch.config(state=ACTIVE)
                                     ])

# Create a copyright strip for this application
frame5 = tk.Label(root,bg='blue4',fg="white",text="Copyright © 2021 Swapnil & Priyanka. All right reserve.",font = ("Times", "14", "bold"),justify=LEFT)
frame5.place(relx=0.4, rely=0.95,relwidth = 0.6, relheight = 0.03)
root.mainloop()
