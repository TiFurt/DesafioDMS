# Generated by Django 4.0.3 on 2022-03-26 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('competicao', '0009_remove_disputa_times_disputa_time01_disputa_time02'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultado',
            name='gols',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='competicao.time'),
            preserve_default=False,
        ),
    ]
