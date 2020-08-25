# Generated by Django 2.2.15 on 2020-08-25 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_auto_20200825_1129'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('text', models.CharField(max_length=3000)),
                ('products', models.ManyToManyField(null=True, to='market.Product')),
            ],
        ),
    ]