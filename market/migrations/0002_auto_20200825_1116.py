# Generated by Django 2.2.15 on 2020-08-25 06:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producttocatalogue',
            name='catalogue',
        ),
        migrations.RemoveField(
            model_name='producttocatalogue',
            name='product',
        ),
        migrations.RemoveField(
            model_name='catalogue',
            name='products',
        ),
        migrations.RemoveField(
            model_name='user',
            name='orders',
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='product',
            name='catalogue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.Catalogue'),
        ),
        migrations.DeleteModel(
            name='OrderForUser',
        ),
        migrations.DeleteModel(
            name='ProductToCatalogue',
        ),
    ]
