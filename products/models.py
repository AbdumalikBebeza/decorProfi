from django.db import models
from django_resized import ResizedImageField


class Catalog(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')
    image = models.ImageField(verbose_name='Фотография (обязательно)')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class SubCatalog(models.Model):
    name = models.CharField(max_length=120, verbose_name='Название Подкатегории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


class Brand(models.Model):
    name = models.CharField(max_length=120, verbose_name='Название бренда')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    articul = models.CharField(max_length=30, verbose_name='Артикул')
    model = models.CharField(max_length=150, verbose_name='Модель')
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, related_name='products',
                                verbose_name='Категория продукта')
    sub_catalog = models.ForeignKey(SubCatalog, on_delete=models.CASCADE, related_name='products',
                                    verbose_name='Подкатегориия продукта')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products',
                              verbose_name='Бренд продукта')
    description = models.TextField(verbose_name='Описание')
    color = models.CharField(max_length=50, verbose_name='Цвет')
    image1 = models.ImageField(verbose_name='Фотография 1 (обязательно)')
    image2 = models.ImageField(verbose_name='Фотография 2 (необязательно)', null=True, blank=True)
    image3 = models.ImageField(verbose_name='Фотография 3 (необязательно)', null=True, blank=True)
    image4 = models.ImageField(verbose_name='Фотография 4 (необязательно)', null=True, blank=True)
    information = models.TextField(verbose_name='Дополнительная информация(размер)')
    price = models.FloatField(verbose_name='Цена')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    @property
    def catalog_name(self):
        return self.catalog.name

    @property
    def brand_name(self):
        return self.brand.name

    @property
    def sub_catalog_name(self):
        return self.sub_catalog.name

    @property
    def catalog_image(self):
        return self.catalog.image
