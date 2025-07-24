from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://kopikenangan.com/")
time.sleep(5)

elements = driver.find_elements(By.XPATH, "//*")

hasil = []

for el in elements:
    try:
        tag = el.tag_name
        el_id = el.get_attribute("id")
        el_class = el.get_attribute("class")

        if el_id or el_class:
            id_str = f"ID: {el_id}" if el_id else "ID: -"
            class_str = f"Class: {el_class}" if el_class else "Class: -"
            hasil.append(f"Tag: {tag} | {id_str} | {class_str}")
    except:
        continue

with open("hasil_element_selenium.txt", "w", encoding="utf-8") as f:
    for line in hasil:
        f.write(line + "\n")

print("✅ Berhasil menyimpan elemen ke hasil_element_selenium.txt")

driver.quit()
