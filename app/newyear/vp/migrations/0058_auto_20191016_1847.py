# Generated by Django 2.2.6 on 2019-10-16 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vp', '0057_auto_20191015_2220'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeBox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('box', models.CharField(db_index=True, max_length=50, verbose_name='Упаковка')),
            ],
            options={
                'verbose_name': 'Вид упаковки',
                'verbose_name_plural': 'Виды упаковок',
                'ordering': ['box'],
            },
        ),
        migrations.RemoveField(
            model_name='classic',
            name='lists',
        ),
        migrations.RemoveField(
            model_name='classic',
            name='sweet',
        ),
        migrations.RemoveField(
            model_name='premium',
            name='lists',
        ),
        migrations.DeleteModel(
            name='Sweet',
        ),
        migrations.AddField(
            model_name='classic',
            name='typebox',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='vp.TypeBox', verbose_name='Вид упаковки'),
        ),
    ]
