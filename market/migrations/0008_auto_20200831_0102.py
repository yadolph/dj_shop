# Generated by Django 2.2.15 on 2020-08-30 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0007_product_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(default='pics/nopic.jpg', upload_to='pics/%Y/%m/%d'),
        ),
    ]