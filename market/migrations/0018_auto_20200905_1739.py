# Generated by Django 2.2.15 on 2020-09-05 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0017_auto_20200905_1732'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topcat',
            options={'verbose_name': 'Top level catalogue', 'verbose_name_plural': 'Top level catalogues'},
        ),
        migrations.AddField(
            model_name='catalogue',
            name='top_level_cat',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='catalogues', to='market.TopCat'),
        ),
    ]