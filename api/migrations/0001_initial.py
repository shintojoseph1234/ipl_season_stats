# Generated by Django 2.0.13 on 2019-11-30 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deliveries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batsman', models.CharField(max_length=255)),
                ('fielder', models.CharField(max_length=255)),
                ('batsman_runs', models.CharField(max_length=255)),
                ('dismissal_kind', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Matches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.IntegerField()),
                ('winner', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('venue', models.CharField(max_length=255)),
                ('toss_winner', models.CharField(max_length=255)),
                ('toss_decision', models.CharField(max_length=255)),
                ('win_by_runs', models.CharField(max_length=255)),
                ('win_by_wickets', models.CharField(max_length=255)),
                ('player_of_match', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='deliveries',
            name='match_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Matches'),
        ),
    ]