import requests
from bs4 import BeautifulSoup


headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
url = "https://notebook.uz/category/Noutbuki_v_Tashkente/lenovo/?Brand=80&sort=stock&order=desc"
response = requests.get(url, headers=headers)
html = response.text
soup = BeautifulSoup(html,'html.parser')
main = soup.find("ul",class_="product-list")
main_block = main.find_all("li")
for product in main_block:
    product_name = product.find("h5").get_text()
    product_price = product.find("span", class_="price").get_text
    product_img = product.find("div",class_="badge-wrapper").find("img")["scr"]




















# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
#
# data_Base = []
# host = "https://notebook.uz/"
# url = "https://notebook.uz/category/Noutbuki_v_Tashkente/lenovo/?Brand=80&sort=stock&order=desc"
# response = requests.get(url, headers=headers)
#
# html = response.text
#
# soup = BeautifulSoup(html, 'html.parser')
# main = soup.find("ul", class_="product-list")
# main_block = main.find_all("li")
# for product in main_block:
#     product_name = product.find("h5").get_text()
#
#     product_price = product.find("div", class_="pricing").find("span", class_="price").get_text()
#     product_image = host + product.find("div", class_="badge-wrapper").find("img")["src"]
#     payment = product.find("span", class_="summary").get_text()
#
#     data_Base.append({
#         "Product_name": product_name,
#         "Product_price": product_price,
#         "Payment": payment
#     })
#
# # print(data_Base[2]["Payment"])






