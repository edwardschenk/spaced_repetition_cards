# Generated by Django 4.2.4 on 2023-09-07 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_card_last_time_correct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='last_time_correct',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]