import requests
from bs4 import BeautifulSoup

URL = "https://www.itproportal.com/features/top-10-essential-technology-trends-you-must-follow-in-2022/"

response = requests.get(URL)

website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

top_tech = soup.find_all(name="h2")
top_tech.pop()

top_10_list = [item.get_text() for item in top_tech]
print(top_10_list)

with open("top-10-tech.txt", mode="w") as file:
    for item in top_10_list:
        file.write(f"{item}\n")