# Generated by Django 3.2.6 on 2021-09-08 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_alter_category_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='sub_Category_name',
            field=models.CharField(default='', max_length=200, unique=True),
        ),
    ]
