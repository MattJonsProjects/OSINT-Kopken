from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://kopikenangan.com/")
time.sleep(5) 

try:
    logo = driver.find_element(By.CLASS_NAME, "logo")
    print("Logo class name:", logo.get_attribute("class"))
except:
    print("Logo tidak ditemukan.")

buttons = driver.find_elements(By.TAG_NAME, "button")
for i, btn in enumerate(buttons):
    print(f"Tombol {i+1}: {btn.text}")

try:
    footer = driver.find_element(By.CLASS_NAME, "footer")
    print("Footer ditemukan.")
except:
    print("Footer tidak ditemukan.")

driver.quit()
