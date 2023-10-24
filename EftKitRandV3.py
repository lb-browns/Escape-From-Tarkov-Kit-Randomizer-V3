from bs4 import BeautifulSoup
from io import StringIO
import requests
import pandas as pd
import numpy as np

def getRandomHelmet():
 helmetWikiLink = 'https://escapefromtarkov.fandom.com/wiki/Headwear'

 helmetSoupA = BeautifulSoup(requests.get(helmetWikiLink).content, 'html.parser')

 helmetDF = []

 for i in helmetSoupA.select(".wikitable"):
    for hr in i.select("hr"):
     hr.replace_with(", ")
    helmetDf = pd.read_html(StringIO(str(i)))[0]
    helmetTitle = i.find_previous("h2").span.text
    helmetDf["helmet_type"] = helmetTitle
    helmetDF.append(helmetDf)

 helmetDf_out = pd.concat(helmetDF)
 print(helmetDf_out)
 randHelm = helmetDf_out.sample(n=1)

 print(randHelm[["Name", "Icon"]])



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

 print (randGun[["Name", "Image"]])

 #Simple Way To Do This
 #reqWeapons = requests.get(weaponWikiLink, "lxml")
 #weaponsSoup = BeautifulSoup(reqWeapons.content)
 #weaponsTableA = weaponsSoup.find_all(name='table')

 #dfAR = pd.read_html(str(weaponsTableA))[0]
 #dfAR.head()
 #dfSMG = pd.read_html(str(weaponsTableA))[1]
 #dfSMG.head()

 #print (dfAR)
 #print (dfSMG)
    

getRandomGun()
getRandomHelmet()