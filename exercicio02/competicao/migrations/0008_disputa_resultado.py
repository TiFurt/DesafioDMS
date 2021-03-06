# Generated by Django 4.0.3 on 2022-03-26 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('competicao', '0007_time_nome_alter_time_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disputa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(verbose_name='Data')),
                ('horario', models.TimeField(verbose_name='Hora')),
                ('local', models.CharField(max_length=100, verbose_name='Local')),
                ('times', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competicao.time')),
            ],
        ),
        migrations.CreateModel(
            name='Resultado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partida', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='competicao.disputa')),
            ],
        ),
    ]
