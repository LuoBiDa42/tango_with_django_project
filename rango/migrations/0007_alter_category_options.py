# Generated by Django 3.2.5 on 2021-07-30 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0006_alter_category_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
