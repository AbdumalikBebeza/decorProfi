from django.db import models
from django_resized import ResizedImageField


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    articul = models.CharField(max_length=30, verbose_name='Артикул')
    model = models.CharField(max_length=150, verbose_name='Модель')
    description = models.TextField(verbose_name='Описание')
    color = models.CharField(max_length=50, verbose_name='Цвет')
    image1 = ResizedImageField(size=[200, 200], force_format='PNG', crop=['middle', 'center'], quality=75,
                               upload_to='media', verbose_name='Фотография 1 (обязательно)')
    image2 = ResizedImageField(size=[200, 200], force_format='PNG', crop=['middle', 'center'], quality=75,
                               upload_to='media', verbose_name='Фотография 2 (не обязательно)', null=True, blank=True)
    image3 = ResizedImageField(size=[200, 200], force_format='PNG', crop=['middle', 'center'], quality=75,
                               upload_to='media', verbose_name='Фотография 3 (не обязательно)', null=True, blank=True)
    image4 = ResizedImageField(size=[200, 200], force_format='PNG', crop=['middle', 'center'], quality=75,
                               upload_to='media', verbose_name='Фотография 4 (не обязательно)', null=True, blank=True)
    information = models.TextField(verbose_name='Дополнительная информация(размер)')
    price = models.FloatField(verbose_name='Цена')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'