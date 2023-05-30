from django.core.management.base import BaseCommand
from bboard.models import Bboard
from agent.models import Agent
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

            creation_date = el.find('creation-date').text
            creation_date = creation_date.split('T')
            part_2 = creation_date[1].split('+')
            part_3 = part_2[0]
            creation_date = f'{creation_date[0]} {part_3}'

            last_update_date = el.find('last-update-date').text
            last_update_date = last_update_date.split('T')
            part_4 = last_update_date[1].split('+')
            part_5 = part_4[0]
            last_update_date = f'{last_update_date[0]} {part_5}'
            # print(creation_date)

            if el.find('internet') != None:
                internet = el.find('internet').text
            else:
                internet = None
            if el.find('parking') != None:
                parking = el.find('parking').text

            else:
                parking = None

            #   вытаскиваем инфу агента
            sales_agent = el.find('sales-agent')
            name = sales_agent.find('name').text
            phone = sales_agent.find('phone').text
            category_agent = sales_agent.find('category').text
            organization = sales_agent.find('organization').text
            email = sales_agent.find('email').text
            if el.find('photo') != None:
                photo = sales_agent.find('photo').text
            else:
                photo = None


            models_agent = Agent.objects.get_or_create(
                name=name,
                phone=phone,
                category=category_agent,
                organization=organization,
                email=email,
                photo=photo,
            )
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
                sales_agent=models_agent,
                internet=internet,
                parking=parking,
                creation_date=creation_date,
                last_update_date=last_update_date,
            )
            models_pars.save()
            # models_agent.save()
        self.stdout.write(self.style.SUCCESS('Данные успешно импортированы'))
