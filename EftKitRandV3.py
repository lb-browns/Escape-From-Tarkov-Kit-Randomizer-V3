from bs4 import BeautifulSoup
from io import StringIO
import requests
import pandas as pd
import numpy as np
import tkinter as tk

window = tk.Tk()
window.title("Escape From Tarkov Kit Randomizer")
window.geometry("800x500")

weaponLabel = tk.Label(window, text="weapon")
backpackLabel = tk.Label(window, text="backpack")
armorLabel = tk.Label(window, text="armor")
rigLabel = tk.Label(window, text="rig")
helmetLabel = tk.Label(window, text="helmet")


def getRandomGun():
 weaponWikiLink = 'https://escapefromtarkov.fandom.com/wiki/Weapons'

 weaponSoupA = BeautifulSoup(requests.get(weaponWikiLink).content, 'html.parser')

 weaponDF = []

 for i in weaponSoupA.select(".wikitable"):
    for hr in i.select("hr"):
        hr.replace_with(", ")
    df = pd.read_html(StringIO(str(i)))[0]
    title = i.find_previous("h3").span.text
    df["weapon_type"] = title
    weaponDF.append(df)
    

 df_out = pd.concat(weaponDF)

 big_df = pd.concat([df_out[df_out['weapon_type'].isin(["Shotguns", "Submachine guns", 
                                                       "Light machine guns", "Assault carbines", 
                                                       "Assault rifles", "Designated marksman rifles", 
                                                       "Sniper rifles", "Pistols"])]])
 big_df.reset_index(drop=True, inplace=True)

 randGun = big_df.sample(n=1)

 return randGun[["Name"]]

 #Other Way To Do This Just Listen To Compiler
 #reqWeapons = requests.get(weaponWikiLink, "lxml")
 #weaponsSoup = BeautifulSoup(reqWeapons.content)
 #weaponsTableA = weaponsSoup.find_all(name='table')

 #dfAR = pd.read_html(str(weaponsTableA))[0]
 #dfAR.head()
 #dfSMG = pd.read_html(str(weaponsTableA))[1]
 #dfSMG.head()

 #print (dfAR)
 #print (dfSMG)

def getRandomHelmet():
 helmetWikiLink = 'https://escapefromtarkov.fandom.com/wiki/Headwear'

 headwearSoupA = BeautifulSoup(requests.get(helmetWikiLink).content, 'html.parser')

 headwearDF = []

 for i in headwearSoupA.select(".wikitable"):
    for hr in i.select("hr"):
        hr.replace_with(", ")
    df = pd.read_html(StringIO(str(i)))[0]
    title = i.find_previous("h2").span.text
    df["headwear_type"] = title
    headwearDF.append(df)
    

 df_out = pd.concat(headwearDF)

 big_df = pd.concat([df_out[df_out['headwear_type'].isin(["Armored", "Vanity"])]])
 big_df.reset_index(drop=True, inplace=True)

 randHeadwear = big_df.sample(n=1)
 
 return randHeadwear[['Name']]

def getRandChestRig():
   chestRigWikiLink = 'https://escapefromtarkov.fandom.com/wiki/Chest_rigs'
   chestRigSoupA = BeautifulSoup(requests.get(chestRigWikiLink).content, 'html.parser')

   chestRigDF = []

   for i in chestRigSoupA.select(".wikitable"):
    for hr in i.select("hr"):
        hr.replace_with(", ")
    df = pd.read_html(StringIO(str(i)))[0]
    title = i.find_previous("h2").span.text
    df["chest_rigs_type"] = title
    chestRigDF.append(df)
    

   df_out = pd.concat(chestRigDF)

   big_df = pd.concat([df_out[df_out['chest_rigs_type'].isin(["Unarmored"])]])
   big_df.reset_index(drop=True, inplace=True)

   randChestRig = big_df.sample(n=1)
   
   return randChestRig[['Name']]

def getRandomAV():
 avWikiLink = 'https://escapefromtarkov.fandom.com/wiki/Armor_vests'

 
 avSoup = BeautifulSoup(requests.get(avWikiLink).content, 'html.parser')
 avTableA = avSoup.find_all(name='table')

 dfAV = pd.read_html(StringIO(str(avTableA)))[0]
 dfAV.head()
 RandAv = dfAV.sample(n=1)

 return RandAv[['Name']]
 
def getRandomBackpack():
 
 backpackWikiLink = 'https://escapefromtarkov.fandom.com/wiki/Backpacks'

 
 backpackSoup = BeautifulSoup(requests.get(backpackWikiLink).content, 'html.parser')
 backpackTableA = backpackSoup.find_all(name='table')

 dfBackpack = pd.read_html(StringIO(str(backpackTableA)))[0]
 dfBackpack.head()
 RandBackpack = dfBackpack.sample(n=1)

 return RandBackpack[['Name']]

def displayWindowText():
  
  weapon = getRandomGun()
  backpack = getRandomBackpack()
  armor = getRandomAV()
  rig = getRandChestRig()
  helmet = getRandomHelmet()

  weaponLabel.config(text=weapon)
  backpackLabel.config(text=backpack)
  armorLabel.config(text=armor)
  rigLabel.config(text=rig)
  helmetLabel.config(text=helmet)



def displayWindow():

  weaponLabel.pack()
  backpackLabel.pack()
  armorLabel.pack()
  rigLabel.pack()
  helmetLabel.pack()

  Tbutton = tk.Button(window, text="Randomize",command=displayWindowText)

  Tbutton.pack()

  window.mainloop()

displayWindow()
