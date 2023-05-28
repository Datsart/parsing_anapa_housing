from django.db import models


# Create your models here.

class Bboard(models.Model):
    rent = models.CharField(max_length=30, verbose_name='Тип объявления')
    category = models.CharField(max_length=30, verbose_name='Вид помещения')
    location = models.CharField(max_length=300, verbose_name='Адрес')
    area_value = models.FloatField(verbose_name='Площадь помещения')
    area_unit = models.CharField(max_length=10, verbose_name='Единица измерения')
    description = models.TextField(max_length=3000, verbose_name='Описание')
    rooms = models.IntegerField(verbose_name='Количество комнат')
    floor = models.IntegerField(verbose_name='Этаж')
    price = models.IntegerField(verbose_name='Цена')
    period = models.CharField(max_length=15, verbose_name='Период')
    sales_agent = models.CharField(max_length=500, verbose_name='Контакты риелтора')

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявление'
        ordering = ['-price']

    def __str__(self):
        return self.category
