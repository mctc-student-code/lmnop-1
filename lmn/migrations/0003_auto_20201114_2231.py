# Generated by Django 3.1.2 on 2020-11-14 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmn', '0002_auto_20201114_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='posted_date',
            field=models.DateTimeField(),
        ),
    ]
