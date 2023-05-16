from bs4 import BeautifulSoup
import requests
import csv

source = requests.get("https://www.jumia.co.ke/").text
source = source.encode("charmap", errors="replace").decode("charmap")
soup = BeautifulSoup(source, "lxml")

with open("jumia2.csv", "a") as f:
    writer = csv.writer(f)
    writer.writerow(["Product", "Price", "Ratings", "Image URL"])

    for item in soup.find_all("div", class_="itm col"):
        name = item.find("img", class_="img")["alt"]
        price = item.find("div", class_="prc").text
        image_link = item.find("img", class_="img")["data-src"]

        link = item.find("a", class_="core")["href"]
        source_2 = requests.get(f"https://www.jumia.co.ke{link}").text
        source_2 = source_2.encode("charmap", errors="replace").decode("charmap")
        soup_2 = BeautifulSoup(source_2, "lxml")

        ratings = soup_2.find("div", class_="stars _s _al").text

        writer.writerow([name, price, ratings, image_link])
