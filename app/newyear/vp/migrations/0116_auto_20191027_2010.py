# Generated by Django 2.2.6 on 2019-10-27 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vp', '0115_auto_20191026_2303'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='main',
            options={'verbose_name': 'Шапка, логотип, фон, иконка сайта', 'verbose_name_plural': 'Шапка, логотип, фон, иконка сайта'},
        ),
        migrations.AddField(
            model_name='main',
            name='icon',
            field=models.ImageField(blank=True, upload_to='main', verbose_name='Иконка'),
        ),
    ]