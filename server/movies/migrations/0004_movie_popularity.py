# Generated by Django 3.2.13 on 2022-11-22 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20221121_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='popularity',
            field=models.FloatField(default=0, null=True),
        ),
    ]
