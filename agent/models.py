from django.db import models


# Create your models here.

class Agent(models.Model):
    name = models.CharField(max_length=20, verbose_name='Имя риелтора')
    phone = models.CharField(max_length=12, verbose_name='Телефон')
    category = models.CharField(max_length=20, verbose_name='Категория арендадатора')
    organization = models.CharField(max_length=30, verbose_name='Организация')
    email = models.CharField(max_length=40, verbose_name='Email')
    photo = models.TextField(verbose_name='Ссылка на фото', null=True, blank=True)

    # bboard = models.ForeignKey(Bboard, verbose_name='Объявления', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Агенты'
        verbose_name = 'Агент'
        ordering = ['-organization']

    def __str__(self):
        return self.name
