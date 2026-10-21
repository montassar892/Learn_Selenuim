from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import pandas as pd


driver = webdriver.Chrome()
driver.get("https://www.yelp.fr/search?find_desc=dentists&find_loc=San+Francisco%2C+CA%2C+%C3%89tats-Unis")
driver.maximize_window()
# Accept cookies 
cookies = driver.find_element(By.ID, "onetrust-accept-btn-handler")
try:
    cookies.click()
except:
    pass
#names
names = driver.find_elements(By.XPATH,'//h3[@class="y-css-hdru7z"]/a')
for name in names:
    print(name.text) 

print('*******')
#addresses
adresses = driver.find_elements(By.XPATH,'//span[@class="y-css-14rmtvr"]')
for adress in adresses:
    print(adress.text)

print('*******')
#expertise

expertise = driver.find_elements(By.XPATH,'//div[@class="y-css-15zfyoa"]')
expertise_list = []
for spec in expertise:
    sp = spec.find_elements(By.XPATH,'.//div[@class="y-css-1ve2u48"]/a/button/p') 
    sp_text = [s.text for s in sp]
    print(sp_text)
    combined_sp = ", ".join(sp_text)
    expertise_list.append(combined_sp)

for e in expertise_list:
    print(e)

print('*******')
#rating
ratings = driver.find_elements(By.XPATH,'//div[@class="y-css-d77n9h"]/span[@class="y-css-qgqb98"]')
for r in ratings:
    print(r.text)


df = pd.DataFrame(columns=["Name","Adresse","Rating","Expertise"])

names_List = []
address_List = []
#expertise_List = []
ratings_List = []

for n in names:
    names_List.append(n.text)
for a in adresses:
    address_List.append(a.text)
for r in ratings:
    ratings_List.append(r.text)

dict_info = {"Name": names_List,
        "Adresse": address_List,
        "Expertise": expertise_list,
        "Rating": ratings_List
        }

df = pd.DataFrame.from_dict(dict_info)
print(df)

df.to_excel('data.xlsx', index = False)