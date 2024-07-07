from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import os
import time

def product_page_info():
    driver = webdriver.Chrome()
    product_list = os.listdir("Search_page_data")
    j = 0

    for i in product_list:
        try:
            with open(f"Search_page_data/{i}", "r", encoding="utf-8", errors="ignore") as file:
                html_doc = file.read()
        except UnicodeDecodeError:
            with open(f"Search_page_data/{i}", "r", encoding="latin-1", errors="ignore") as file:
                html_doc = file.read()

        html_soup = BeautifulSoup(html_doc, "html.parser")
        link = html_soup.find("a")
        
        if link is not None:
            href = link.get("href")
            if href:
                url = "https://www.amazon.in" + href
                driver.get(url)
                time.sleep(2)  

                try:
                    elem = driver.find_element(By.CLASS_NAME, "centerColAlign")
                    data = elem.get_attribute("innerHTML")

                    if not os.path.exists("Product_data_"):
                        os.makedirs("Product_data_")

                    with open(f"Product_data_/product_{j}.html", "w", encoding="utf-8") as f:
                        f.write(data)
                    j += 1

                except Exception as e:
                    print(f"Error while scraping product page: {e}")
            else:
                print(f"No href attribute found for the link in file: {i}")
        else:
            print(f"No <a> tag found in file: {i}")
    time.sleep(10)

    driver.quit()

