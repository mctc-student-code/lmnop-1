# Generated by Django 3.1.2 on 2020-11-18 00:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lmn', '0006_auto_20201116_2259'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='show',
            unique_together={('show_date', 'artist', 'venue')},
        ),
    ]
