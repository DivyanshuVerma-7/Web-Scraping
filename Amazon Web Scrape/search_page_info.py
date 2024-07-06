from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def search_page_info():
    product = "Bluetooth Earbuds"
    driver = webdriver.Chrome()
    file = 0
    for i in range (1, 6):
        URL = f"https://www.amazon.in/s?k={product}&page={i}&crid=3FGKXS4TI77FA&qid=1720166871&sprefix=laptop%2Caps%2C230&ref=sr_pg_2"
        driver.get(URL)



        result_items = driver.find_elements(By.CSS_SELECTOR, ".a-size-mini.a-spacing-none.a-color-base.s-line-clamp-2")
        for item in result_items:
            data = item.get_attribute("outerHTML")
            with open(f"Search_page_data/{product}_{file}.html","w",encoding="utf-8") as f:
                f.write(data)
                file += 1
                print(f"File-{file} created")
        time.sleep(10)
            