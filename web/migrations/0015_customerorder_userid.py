# Generated by Django 3.2.6 on 2021-09-12 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0014_signup'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerorder',
            name='userid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='web.signup'),
        ),
    ]
