# Generated by Django 4.1 on 2022-08-16 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itpark', '0002_alter_itpark_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itpark',
            name='volume',
            field=models.CharField(max_length=100, verbose_name='Объем финансирования'),
        ),
    ]
