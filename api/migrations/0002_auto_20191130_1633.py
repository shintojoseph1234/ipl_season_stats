# Generated by Django 2.0.13 on 2019-11-30 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matches',
            name='win_by_runs',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='matches',
            name='win_by_wickets',
            field=models.IntegerField(),
        ),
    ]
