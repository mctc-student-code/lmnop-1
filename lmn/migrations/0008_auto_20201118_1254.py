# Generated by Django 3.1.2 on 2020-11-18 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmn', '0007_auto_20201118_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='venue',
            unique_together={('name', 'city', 'state')},
        ),
    ]