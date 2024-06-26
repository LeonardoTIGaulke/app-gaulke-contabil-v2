# Generated by Django 4.2.6 on 2024-05-16 19:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_gaulke_contabil_v2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model_tb_clients',
            name='cod_sistema',
            field=models.CharField(default='', max_length=8),
        ),
        migrations.AlterField(
            model_name='model_tb_clients',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 16, 16, 27, 55, 93402)),
        ),
        migrations.AlterField(
            model_name='model_tb_clients',
            name='update_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 16, 16, 27, 55, 93402)),
        ),
        migrations.AlterField(
            model_name='model_tb_imposto_de_renda',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 16, 16, 27, 55, 93402)),
        ),
        migrations.AlterField(
            model_name='model_tb_imposto_de_renda',
            name='update_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 16, 16, 27, 55, 93402)),
        ),
        migrations.AlterField(
            model_name='model_tb_imposto_de_renda',
            name='valor_ano_anterior',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AlterField(
            model_name='model_tb_imposto_de_renda',
            name='valor_ano_atual',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AlterField(
            model_name='model_tb_imposto_de_renda_comments',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 16, 16, 27, 55, 93402)),
        ),
        migrations.AlterField(
            model_name='model_tb_imposto_de_renda_comments',
            name='update_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 16, 16, 27, 55, 93402)),
        ),
    ]
