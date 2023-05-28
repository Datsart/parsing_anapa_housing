import requests
from bs4 import BeautifulSoup

response = requests.get('https://yugcity.yucrm.ru/export/advertise?portal=yandex&mediaplan=33&hash=3ad1257e')
soup = BeautifulSoup(response.content, 'lxml')
all_board = soup.find_all('offer')
# print(all_board)
for el in all_board:
    rent = el.find('type').text
    property_type = el.find('property-type').text
    category = el.find('category').text
    location = el.find('location').text
    # print(location)
    area = el.find_all('area')
    # image = el.find('image').text
    print(area)
    description = el.find('description').text
    # print(description)