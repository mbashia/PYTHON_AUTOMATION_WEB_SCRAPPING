from bs4 import BeautifulSoup
import requests


# function to append data to text file
def append_file(file, content):
    with open(file, 'a') as f:
        f.write(content)


# initializing the url and creating the beautiful soup object
url = 'https://www.jumia.co.ke/catalog/?q=iphone+phone'
response = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')
# getting a list of all items
phone_list = soup.find_all("a", class_="core")

# looping through the items
for item in phone_list:

    phone_name = item.find("h3", class_="name").text
    # print(phone_name)

    phone_price = item.find("div", class_="prc").text

    # print(phone_price)

    try:
        phone_discount = item.find("div", class_="bdg _dsct _sm").text
        # print(f'Allowable discount:{phone_discount}')

    except:
        phone_discount = 0

    try:
        seller_rating = item.find("div", class_="stars _s").text
        # print(f'seller_Rating:{seller_rating}')
    except:
        print("seller rating not available at the moment")
    phone_link = item.attrs["href"]
    # print(phone_link)

    # print(" ")
    phone_info = f'''\n\n
\nphone name:{phone_name}
phone price:{phone_price}
phone discount:{phone_discount}
phone link:{phone_link}\n
\n

       '''
    phone_info_stripped = phone_info.rstrip()

    append_file("iphone .txt", phone_info_stripped)
