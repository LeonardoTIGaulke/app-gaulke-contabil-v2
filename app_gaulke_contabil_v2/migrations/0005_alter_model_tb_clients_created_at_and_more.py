# Generated by Django 4.2.6 on 2024-05-21 16:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_gaulke_contabil_v2', '0004_alter_model_tb_clients_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model_tb_clients',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 21, 13, 31, 16, 870330)),
        ),
        migrations.AlterField(
            model_name='model_tb_clients',
            name='update_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 21, 13, 31, 16, 870330)),
        ),
        migrations.AlterField(
            model_name='model_tb_imposto_de_renda',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 21, 13, 31, 16, 871328)),
        ),
        migrations.AlterField(
            model_name='model_tb_imposto_de_renda',
            name='update_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 21, 13, 31, 16, 871328)),
        ),
        migrations.AlterField(
            model_name='model_tb_imposto_de_renda_comments',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 21, 13, 31, 16, 871328)),
        ),
        migrations.AlterField(
            model_name='model_tb_imposto_de_renda_comments',
            name='update_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 21, 13, 31, 16, 871328)),
        ),
        migrations.AlterField(
            model_name='model_tb_imposto_de_renda_comments',
            name='username',
            field=models.CharField(max_length=155),
        ),
    ]
