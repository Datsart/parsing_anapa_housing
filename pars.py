import requests
from bs4 import BeautifulSoup

response = requests.get('https://yugcity.yucrm.ru/export/advertise?portal=yandex&mediaplan=33&hash=3ad1257e')
soup = BeautifulSoup(response.content, 'lxml')
all_board = soup.find_all('offer')
# print(all_board)
for el in all_board:
    rent = el.find('type').text
    category = el.find('category').text
    location = el.find('location').text
    area_value = float(el.find('value').text)
    area_unit = el.find('unit').text
    # image = el.find('image').text
    description = el.find('description').text
    rooms = int(el.find('rooms').text)
    floor = int(el.find('floor').text)
    price = int(el.find('price').find('value').text)
    period = el.find('period').text
    sales_agent = el.find('sales-agent').text

    internet = el.find('internet')

    if internet is not None:
        internet = internet.text
        print(internet)
    else:
        internet = None
        print('лох')

