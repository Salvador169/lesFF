# Generated by Django 4.0.3 on 2022-07-03 22:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegistoMovimento',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('matricula', models.CharField(blank=True, db_column='Matricula', max_length=255, null=True)),
                ('data_de_entrada', models.DateTimeField(db_column='Data de entrada', default=datetime.datetime.now)),
                ('data_de_saida', models.DateTimeField(blank=True, db_column='Data de saida', null=True)),
                ('provas', models.CharField(blank=True, db_column='Provas', max_length=255, null=True)),
            ],
            options={
                'db_table': 'RegistoMovimento',
            },
        ),
        migrations.CreateModel(
            name='TabelaMatriculas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pais', models.CharField(db_column='Pais', max_length=255)),
                ('formato', models.CharField(db_column='Formato', max_length=255)),
            ],
            options={
                'db_table': 'TabelaMatriculas',
            },
        ),
        migrations.CreateModel(
            name='Viatura',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('marca', models.CharField(blank=True, db_column='Marca', max_length=255, null=True)),
                ('modelo', models.CharField(blank=True, db_column='Modelo', max_length=255, null=True)),
                ('matricula', models.CharField(blank=True, db_column='Matricula', max_length=255, null=True)),
            ],
            options={
                'db_table': 'Viatura',
            },
        ),
    ]
