# Generated by Django 2.2.6 on 2019-10-15 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vp', '0039_auto_20191015_1948'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classic',
            old_name='image',
            new_name='images',
        ),
        migrations.RenameField(
            model_name='premium',
            old_name='image',
            new_name='images',
        ),
    ]
