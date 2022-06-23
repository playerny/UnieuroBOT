import time

import os
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import tinyWinToast.tinyWinToast as Toast

cdir = os.getcwd()
ser = Service("C:\ChromeDriver\chromedriver.exe")
options = webdriver.ChromeOptions()
# options.headless = True
driver = webdriver.Chrome(service=ser, options=options)

def readCrd():
    txt = open("var.txt").read()
    user = txt.split(",")[0]
    pwd = txt.split(",")[1]
    url = txt.split(",")[2]
    return user,pwd,url

def login():
    user,pwd,url = readCrd()
    driver.get("https://www.unieuro.it/online/login") #Unieuro pagina di login
    time.sleep(2)
    biscotto = driver.find_element(By.ID, "onetrust-reject-all-handler")
    biscotto.click()
    username = driver.find_element(By.ID, "j_username")
    username.send_keys(user)
    username.send_keys(Keys.RETURN)
    #time.sleep(5)
    password = driver.find_element(By.ID, "j_password")
    password.send_keys(pwd)
    password.send_keys(Keys.RETURN)
    #time.sleep(2)
    #os.system("pause")
    availability()

def availability():
    user,pwd,url = readCrd()
    driver.get(url)
    #time.sleep(5)
    # biscotto = driver.find_element(By.ID, "onetrust-reject-all-handler")
    # biscotto.click()
    avb = driver.find_element(By.CLASS_NAME, "pdp-right__buttons-container")
    avb = avb.text
    print(avb)
    x = 0
    if ("AGGIUNGI AL CARRELLO" in avb):
        Toast.getToast("Il prodotto è disponibile!", "Sto aggiungendo il prodotto al carrello!!!",cdir + "\\unieuro.ico", iconCrop="circle", appId= "Unieuro BOT").show()
        print(str(x) + ": Prodotto disponibile! ")
        x = x + 1
        checkout()

    while ("NOTIFICA DISPONIBILITÀ" in avb):
        print(str(x) + ": Prodotto non disponibile. ")
        x = x + 1
        time.sleep(1)
        driver.get(url)
        avb = driver.find_element(By.CLASS_NAME, "pdp-right__buttons-container")
        avb = avb.text

def checkout():
    print("Sono al checkout")
    buyButton = driver.find_element(By.CLASS_NAME, "icon-tool-cart")
    buyButton.click()
    time.sleep(1)
    driver.get("https://www.unieuro.it/online/checkout/delivery") #Pagina di checkout
    checkoutBtn1 = driver.find_element(By.CLASS_NAME, "icon-arrow-right") #Metodo Spedizione
    checkoutBtn1.click()
    time.sleep(1)
    checkoutBtn2 = driver.find_element(By.XPATH, "//*[@id='"'anchor-home'"']/div[2]/div[4]/button/i") #Indirizzo Spedizione
    checkoutBtn2.click()
    time.sleep(1)
    checkoutBtn3 = driver.find_element(By.XPATH, "//*[@id='"'payment'"']/i") #Servizi aggiuntivi di spedizione
    checkoutBtn3.click()
    time.sleep(1)
    checkoutBtn4 = driver.find_element(By.XPATH, "//*[@id='"'modifyBillingDataForm'"']/section/div[2]/button/i") #Scontrino
    checkoutBtn4.click()
    Toast.getToast("Manca poco!", "Il prodotto è stato aggiunto al carrello, resta solo da confermare il pagamento.",cdir + "\\unieuro.ico", iconCrop="circle", appId= "Unieuro BOT").show()
    #os.system("pause")

login()
