# Generated by Django 2.2.6 on 2019-10-27 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nba', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='away_score',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='home_score',
            field=models.FloatField(null=True),
        ),
    ]