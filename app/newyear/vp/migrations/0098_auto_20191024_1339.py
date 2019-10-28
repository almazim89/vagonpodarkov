# Generated by Django 2.2.6 on 2019-10-24 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vp', '0097_auto_20191021_1936'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilesLoad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, default='', max_length=150, verbose_name='Название')),
                ('media', models.ImageField(blank=True, upload_to='files', verbose_name='Файл')),
            ],
            options={
                'verbose_name': 'Название | Формат',
                'verbose_name_plural': 'Файлы',
            },
        ),
        migrations.AddField(
            model_name='classic',
            name='files',
            field=models.CharField(db_index=True, default='', max_length=150, verbose_name='Файл'),
        ),
        migrations.AddField(
            model_name='premium',
            name='files',
            field=models.CharField(db_index=True, default='', max_length=150, verbose_name='Файл'),
        ),
    ]
