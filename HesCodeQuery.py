from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from time import time, sleep
import time
import json  # Verilerin json formatında olmasından dolayı kullanılır.


tcKimlik = str(input("Tc Kimlik:\n"))
sifre = str(input("Şifre:\n"))

driver = webdriver.Chrome(executable_path="C:\\seleniumbrowserdriverSave\\chromedriver.exe")
driver.get("https://www.turkiye.gov.tr/saglik-bakanligi-hes-kodu-sorgulama")
login = driver.find_element_by_xpath("//*[@id='contentStart']/div/div[2]/a")
login.click()
time.sleep(3)

driver.find_element_by_name("tridField").send_keys(tcKimlik)
time.sleep(3)
driver.find_element_by_name("egpField").send_keys(sifre)
time.sleep(3)
driver.find_element_by_name("submitButton").click()
time.sleep(3)

### HES kodu işlemleri sonlandırılması dolayısıyla toplu hes kodu sorgusu yapılamadı.