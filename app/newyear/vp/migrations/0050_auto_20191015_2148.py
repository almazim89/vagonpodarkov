# Generated by Django 2.2.6 on 2019-10-15 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vp', '0049_auto_20191015_2141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classic',
            name='lists',
        ),
        migrations.AddField(
            model_name='classic',
            name='sweets',
            field=models.ForeignKey(default='Список', on_delete=django.db.models.deletion.CASCADE, to='vp.Sweets'),
        ),
    ]