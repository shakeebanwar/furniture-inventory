# Generated by Django 3.2.6 on 2021-09-08 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_alter_brand_brandname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='Category_name',
            field=models.CharField(default='', max_length=200, unique=True),
        ),
    ]
