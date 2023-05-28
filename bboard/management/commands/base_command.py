from django.core.management.base import BaseCommand
from bboard.models import Bboard

import requests
from bs4 import BeautifulSoup


class Command(BaseCommand):
    help = 'Парсинг объявлений в модель'

    def handle(self, *args, **options):
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
            # internet = str(el.find('internet').text)
            # parking = str(el.find('parking').text)

            models_pars = Bboard(
                rent=rent,
                category=category,
                location=location,
                area_value=area_value,
                area_unit=area_unit,
                description=description,
                rooms=rooms,
                floor=floor,
                price=price,
                period=period,
                sales_agent=sales_agent,
                # internet=internet,
                # parking=parking,
            )
            models_pars.save()
            self.stdout.write(self.style.SUCCESS('Данные успешно импортированы'))
