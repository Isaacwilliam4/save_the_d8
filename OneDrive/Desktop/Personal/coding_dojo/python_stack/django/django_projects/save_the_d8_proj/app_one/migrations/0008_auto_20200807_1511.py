# Generated by Django 2.2 on 2020-08-07 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_one', '0007_auto_20200807_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gift',
            name='note',
            field=models.TextField(default=''),
        ),
    ]