from bs4 import BeautifulSoup
import os
import pandas as pd
import numpy as np

def csv_creation():
    product_list = os.listdir("Product_data_")

    product_dict = {"Title": [], "Price": [], "Ratings": [], "Total_no_of_Ratings": []}

    for i in product_list:
        try:
            with open(f"Product_data_/{i}", "r", encoding="utf-8", errors="ignore") as file:
                html_doc = file.read()
        except UnicodeDecodeError:
            with open(f"Product_data_/{i}", "r", encoding="latin-1", errors="ignore") as file:
                html_doc = file.read()
        product_soup = BeautifulSoup(html_doc, "html.parser")
        
        # Extract product title
        product_title = product_soup.find("span", attrs={"id": "productTitle"})
        title_value = product_title.text.strip() if product_title else "N/A"
        
        # Extract product price
        product_price = product_soup.find("span", attrs={"class": "a-price-whole"})
        price_value = product_price.text.strip() if product_price else "N/A"
        
        # Extract product rating
        product_rating = product_soup.find("span", attrs={"class": "a-icon-alt"})
        rating_value = product_rating.text.strip() if product_rating else "N/A"
        
        # Extract total number of ratings
        product_total_ratings = product_soup.find("span", attrs={"id": "acrCustomerReviewText"})
        total_ratings_value = product_total_ratings.text.strip() if product_total_ratings else "N/A"
        
        # Append values to the dictionary
        product_dict['Title'].append(title_value)
        product_dict['Price'].append(price_value)
        product_dict['Ratings'].append(rating_value)
        product_dict['Total_no_of_Ratings'].append(total_ratings_value)

    # Create a DataFrame and save to CSV
    df = pd.DataFrame(data=product_dict)
    df["Title"] = df["Title"].replace("N/A", None)
    df = df.dropna(subset=['Title'])
    df.to_csv("Product_data.csv", index=False, header=True)


