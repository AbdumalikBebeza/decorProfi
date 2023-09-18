# Generated by Django 4.2.5 on 2023-09-18 18:19

from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('articul', models.CharField(max_length=30, verbose_name='Артикул')),
                ('model', models.CharField(max_length=150, verbose_name='Модель')),
                ('description', models.TextField(verbose_name='Описание')),
                ('color', models.CharField(max_length=50, verbose_name='Цвет')),
                ('image1', django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format='PNG', keep_meta=True, quality=75, scale=0.5, size=[200, 200], upload_to='media', verbose_name='Фотография 1 (обязательно)')),
                ('image2', django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format='PNG', keep_meta=True, null=True, quality=75, scale=0.5, size=[200, 200], upload_to='media', verbose_name='Фотография 2 (не обязательно)')),
                ('image3', django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format='PNG', keep_meta=True, null=True, quality=75, scale=0.5, size=[200, 200], upload_to='media', verbose_name='Фотография 3 (не обязательно)')),
                ('image4', django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format='PNG', keep_meta=True, null=True, quality=75, scale=0.5, size=[200, 200], upload_to='media', verbose_name='Фотография 4 (не обязательно)')),
                ('information', models.TextField(verbose_name='Дополнительная информация(размер)')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.brand')),
                ('catalog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.catalog')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]
