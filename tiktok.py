from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

driver = webdriver.Chrome(executable_path="D:\\Programming\\Python\\Web Scrawler\\chromedriver.exe")
driver.get("https://www.tiktok.com/")

#tiktoks = driver.find_element(By.CLASS_NAME, "tiktok-1id9666-DivMainContainer")
num1 = 0
i = 958
while i < 1000:
    while num1 < 1000:
        driver.execute_script("window.scrollBy(0,document.body.scrollHeight)", "") 
        num1 = len(driver.find_elements(By.CLASS_NAME, "etvrc4k0"))
        print(num1)
        time.sleep(3)
    num1 = 0
    templist = [] 
    num = driver.find_elements(By.CLASS_NAME, "etvrc4k0")
    for vid in num:
        user = vid.find_element(By.CLASS_NAME, "emt6k1z0").text
        hash = vid.find_element(By.CLASS_NAME, "e1h0bjw60").text
        music = vid.find_element(By.CLASS_NAME, "e11ku0eu0").text
        likes = vid.find_elements(By.CLASS_NAME, "e1pqpokj2")[0].text
        comments = vid.find_elements(By.CLASS_NAME, "e1pqpokj2")[1].text
        shares = vid.find_elements(By.CLASS_NAME, "e1pqpokj2")[2].text
        length = ""
        if(len(vid.find_elements(By.CLASS_NAME, "e1awzrv32")) >0):
            length = vid.find_elements(By.CLASS_NAME, "e1awzrv32")[0].text

        Table_dict={ 'User': user, 'Hash':hash, 'Music':music, 'Likes':likes, 'Comments':comments, 'Shares':shares, 'Length':length}
            
        templist.append(Table_dict) 
        df = pd.DataFrame(templist)

    df.to_csv('1000_'+str(i)+'.csv')
    i+=1
    driver.refresh() 

driver.close()