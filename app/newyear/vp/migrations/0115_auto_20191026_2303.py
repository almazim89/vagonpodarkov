# Generated by Django 2.2.6 on 2019-10-26 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vp', '0114_socials'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.CharField(blank=True, db_index=True, default='', max_length=250, verbose_name='Заголовок 1')),
                ('texts1', models.TextField(blank=True, db_index=True, verbose_name='Текст 1')),
                ('title2', models.CharField(blank=True, db_index=True, default='', max_length=250, verbose_name='Заголовок 2')),
                ('texts2', models.TextField(blank=True, db_index=True, verbose_name='Текст 2')),
                ('mail', models.CharField(blank=True, db_index=True, default='@mail.ru', max_length=250, verbose_name='Почта')),
                ('copy', models.CharField(blank=True, db_index=True, default='', max_length=250, verbose_name='Копирайт')),
            ],
            options={
                'verbose_name': 'Подвал сайта',
                'verbose_name_plural': 'Подвал сайта',
            },
        ),
        migrations.AlterField(
            model_name='classic',
            name='files',
            field=models.CharField(db_index=True, default='', max_length=250, verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='classic',
            name='media',
            field=models.CharField(db_index=True, max_length=250, verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='classic',
            name='title',
            field=models.CharField(db_index=True, max_length=250, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='classic',
            name='typebox',
            field=models.CharField(db_index=True, default='', max_length=250, verbose_name='Тип упаковки'),
        ),
        migrations.AlterField(
            model_name='classicimg',
            name='title',
            field=models.CharField(db_index=True, default='', max_length=250, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='filesload',
            name='title',
            field=models.CharField(db_index=True, default='', max_length=250, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='manufactures',
            name='title',
            field=models.CharField(db_index=True, default='', max_length=250, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='premium',
            name='files',
            field=models.CharField(db_index=True, default='', max_length=250, verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='premium',
            name='media',
            field=models.CharField(db_index=True, max_length=250, verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='premium',
            name='title',
            field=models.CharField(db_index=True, max_length=250, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='premium',
            name='typebox',
            field=models.CharField(db_index=True, default='', max_length=250, verbose_name='Тип упаковки'),
        ),
        migrations.AlterField(
            model_name='premiumimg',
            name='title',
            field=models.CharField(db_index=True, default='', max_length=250, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='sweets',
            name='manufact',
            field=models.CharField(db_index=True, max_length=250, verbose_name='Производитель'),
        ),
        migrations.AlterField(
            model_name='sweets',
            name='title',
            field=models.CharField(db_index=True, max_length=250, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='sweetsimg',
            name='title',
            field=models.CharField(db_index=True, default='', max_length=250, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='title',
            name='h1',
            field=models.CharField(blank=True, db_index=True, default='', max_length=250, verbose_name='Заголовок h1 страницы сайта'),
        ),
        migrations.AlterField(
            model_name='title',
            name='h2',
            field=models.CharField(blank=True, default='', max_length=250, verbose_name='Заголовок h2 страницы сайта'),
        ),
        migrations.AlterField(
            model_name='title',
            name='h3_classic',
            field=models.CharField(blank=True, default='', max_length=250, verbose_name='Заголовок h3 для классики'),
        ),
        migrations.AlterField(
            model_name='title',
            name='h3_premium',
            field=models.CharField(blank=True, default='', max_length=250, verbose_name='Заголовок h3 для премиум'),
        ),
        migrations.AlterField(
            model_name='title',
            name='name_page',
            field=models.CharField(blank=True, db_index=True, default='Сладкие Новогодние подарки для детей 2020', max_length=250, verbose_name='Краткое описание страницы сайта'),
        ),
        migrations.AlterField(
            model_name='title',
            name='title',
            field=models.CharField(db_index=True, default='', max_length=250, verbose_name='Название страницы сайта'),
        ),
        migrations.AlterField(
            model_name='topnumbersleft',
            name='city',
            field=models.CharField(db_index=True, default='', max_length=250, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='topnumbersright',
            name='city',
            field=models.CharField(db_index=True, default='', max_length=250, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='typebox',
            name='title',
            field=models.CharField(db_index=True, default='', max_length=250, verbose_name='Тип упаковки'),
        ),
    ]
