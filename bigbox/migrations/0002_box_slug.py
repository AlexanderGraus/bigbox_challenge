# Generated by Django 2.2 on 2021-05-24 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bigbox', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='box',
            name='slug',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]