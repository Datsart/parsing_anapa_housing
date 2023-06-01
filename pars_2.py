from django.core.management.base import BaseCommand
import requests
from bs4 import BeautifulSoup

response = requests.get('https://yugcity.yucrm.ru/export/advertise?portal=yandex&mediaplan=33&hash=3ad1257e')
soup = BeautifulSoup(response.content, 'lxml')
all_board = soup.find_all('offer')
my_dict = {}
for el in all_board:
    id = el.get('internal-id')
    # print(id)
    my_list = []
    for photo in el.find_all('image'):
        my_list.append(photo.text)
        # print(photo.text)
    my_dict[id] = my_list
for i, j in my_dict.items():
    print(i, j)
