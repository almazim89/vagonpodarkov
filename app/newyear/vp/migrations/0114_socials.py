# Generated by Django 2.2.6 on 2019-10-26 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vp', '0113_topnumbersleft_topnumbersright'),
    ]

    operations = [
        migrations.CreateModel(
            name='Socials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media', models.ImageField(blank=True, upload_to='socials', verbose_name='Изображение')),
                ('urls', models.URLField(default='', max_length=250, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Социальные сети',
                'verbose_name_plural': 'Социальные сети',
            },
        ),
    ]
