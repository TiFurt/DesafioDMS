# Generated by Django 4.0.3 on 2022-03-26 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competicao', '0005_delete_competicao_rename_pontos_time_gols'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='time',
            name='nome',
        ),
        migrations.AlterField(
            model_name='time',
            name='gols',
            field=models.IntegerField(default=0, verbose_name='Gols'),
        ),
        migrations.AlterField(
            model_name='time',
            name='id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='Nome'),
        ),
    ]
