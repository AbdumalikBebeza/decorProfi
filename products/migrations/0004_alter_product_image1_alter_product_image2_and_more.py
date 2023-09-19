# Generated by Django 4.2.5 on 2023-09-19 14:05

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_image1_alter_product_image2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image1',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format='PNG', keep_meta=True, quality=100, scale=0.5, size=[600, 600], upload_to='media', verbose_name='Фотография 1 (обязательно)'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image2',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format='PNG', keep_meta=True, null=True, quality=100, scale=0.5, size=[600, 600], upload_to='media', verbose_name='Фотография 2 (не обязательно)'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image3',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format='PNG', keep_meta=True, null=True, quality=100, scale=0.5, size=[600, 600], upload_to='media', verbose_name='Фотография 3 (не обязательно)'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image4',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format='PNG', keep_meta=True, null=True, quality=100, scale=0.5, size=[600, 600], upload_to='media', verbose_name='Фотография 4 (не обязательно)'),
        ),
    ]
