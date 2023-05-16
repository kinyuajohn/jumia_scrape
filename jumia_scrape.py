from bs4 import BeautifulSoup
import requests
import csv

source = requests.get("https://www.jumia.co.ke/").text
source = source.encode("charmap", errors="replace").decode("charmap")
soup = BeautifulSoup(source, "lxml")

# print(soup)

with open("jumia.csv", "a") as f:
    writer = csv.writer(f)
    writer.writerow(["Product", "Price", "Image URL"])

    for item in soup.find_all("div", class_="itm col"):
        name = item.find("img", class_="img")["alt"]
        # print(name)
        price = item.find("div", class_="prc").text
        # print(price)
        image_link = item.find("img", class_="img")["data-src"]
        # print(image_link)

        writer.writerow([name, price, image_link])
