# Generated by Django 5.1.2 on 2024-11-10 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0002_delete_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='category',
            field=models.CharField(choices=[('vegetable', 'Vegetable'), ('fruit', 'Fruit'), ('herb', 'Herb'), ('flower', 'Flower'), ('cacti', 'Cacti'), ('desert', 'Desert')], max_length=20),
        ),
    ]
