# Generated by Django 2.2.6 on 2019-10-25 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vp', '0107_auto_20191025_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='description2',
            field=models.TextField(blank=True, default='', verbose_name='Краткое описание сайта 2'),
        ),
    ]