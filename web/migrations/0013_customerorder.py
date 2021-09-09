# Generated by Django 3.2.6 on 2021-09-09 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_items_brandid'),
    ]

    operations = [
        migrations.CreateModel(
            name='customerOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(default='', max_length=255)),
                ('lastname', models.CharField(default='', max_length=255)),
                ('streetAdress', models.CharField(default='', max_length=255)),
                ('city', models.CharField(default='', max_length=255)),
                ('phone', models.CharField(default='', max_length=20)),
                ('zipcode', models.CharField(default='', max_length=20)),
                ('ordernote', models.CharField(default='', max_length=300)),
                ('productid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='web.items')),
            ],
        ),
    ]