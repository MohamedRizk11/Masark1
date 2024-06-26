# Generated by Django 5.0.4 on 2024-04-21 20:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masark', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FamousPlace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='station',
            name='famousPlaces',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='stationid',
        ),
        migrations.AddField(
            model_name='ticket',
            name='from_station',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='from_station', to='masark.station'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='to_station',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='to_station', to='masark.station'),
        ),
        migrations.AddField(
            model_name='station',
            name='famous_places',
            field=models.ManyToManyField(to='masark.famousplace'),
        ),
    ]
