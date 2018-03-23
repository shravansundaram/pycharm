import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.amazon.com/Satechi-Aluminum-Type-C-Pro-Adapter/dp/B06XRVX3XM/ref=pd_ybh_a_9?_encoding=UTF8&psc=1&refRID=JMJW4ZEW3Y8M6RQ3ZAJJ")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"id": "priceblock_ourprice", "class": "a-size-medium a-color-price"})
string_price = element.text.strip()

price_without_symbol = string_price[1:]

price = float(price_without_symbol)

if price < 100:
    print("Buy the Damn Thing Already!")
    print("Current price is {}".format(string_price))
else:
    print("Too expensive, don't buy it")





# <span id="priceblock_ourprice" class="a-size-medium a-color-price">$89.99</span>
