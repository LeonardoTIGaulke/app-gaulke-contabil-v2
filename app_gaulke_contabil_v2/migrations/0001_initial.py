# Generated by Django 4.2.6 on 2024-05-15 14:43

import datetime
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Model_tb_apontamento_horas_matriz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_apont', models.CharField(max_length=10)),
                ('horario_inicio', models.CharField(max_length=5)),
                ('horario_fim', models.CharField(max_length=5)),
                ('competencia', models.CharField(max_length=15)),
                ('codigo_empresa', models.CharField(max_length=15)),
                ('razao_social', models.CharField(max_length=155)),
                ('atividade', models.CharField(max_length=25)),
                ('observacao', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=55)),
                ('setor', models.CharField(max_length=15)),
                ('mes', models.CharField(max_length=10)),
                ('ano', models.SmallIntegerField()),
                ('tempo', models.CharField(max_length=18)),
                ('regime', models.CharField(max_length=55)),
                ('regime_agrup', models.CharField(max_length=55)),
                ('tipo_empresa', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Model_tb_clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_sistema', models.CharField(max_length=8)),
                ('contribuinte', models.CharField(max_length=125)),
                ('cpf_cnpj', models.CharField(max_length=18)),
                ('celular', models.CharField(max_length=18)),
                ('telefone', models.CharField(max_length=18)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2024, 5, 15, 11, 43, 55, 761494))),
                ('update_at', models.DateTimeField(default=datetime.datetime(2024, 5, 15, 11, 43, 55, 761494))),
            ],
        ),
        migrations.CreateModel(
            name='Model_tb_imposto_de_renda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.CharField(max_length=4)),
                ('status_smart_IR', models.CharField(max_length=25)),
                ('dificuldade', models.CharField(max_length=25)),
                ('valor_ano_anterior', models.CharField(max_length=25)),
                ('valor_ano_atual', models.CharField(max_length=25)),
                ('situacao_ano_anterior', models.CharField(max_length=55)),
                ('status_pagamento_IR', models.CharField(max_length=3)),
                ('dt_pagamento_IR', models.CharField(max_length=10)),
                ('info_forma_pagamento', models.CharField(max_length=25)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2024, 5, 15, 11, 43, 55, 761494))),
                ('update_at', models.DateTimeField(default=datetime.datetime(2024, 5, 15, 11, 43, 55, 761494))),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_gaulke_contabil_v2.model_tb_clients')),
            ],
        ),
        migrations.CreateModel(
            name='Model_tb_subtasks_apont_horas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.IntegerField()),
                ('data_apont', models.CharField(max_length=10)),
                ('horario_inicio', models.CharField(max_length=5)),
                ('horario_fim', models.CharField(max_length=5)),
                ('atividade', models.CharField(max_length=25)),
                ('observacao', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=55)),
                ('setor', models.CharField(max_length=15)),
                ('mes', models.CharField(max_length=10)),
                ('ano', models.SmallIntegerField()),
                ('tempo', models.CharField(max_length=18)),
                ('regime', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Model_tb_users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('first_name', models.CharField(max_length=25)),
                ('full_name', models.CharField(max_length=155)),
                ('sector', models.CharField(max_length=55)),
                ('password', models.CharField(max_length=128)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sessao_atividades', models.SmallIntegerField()),
                ('sessao_relatorios', models.SmallIntegerField()),
                ('sessao_imposto_de_renda', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Model_tb_imposto_de_renda_comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25)),
                ('comment', models.CharField(max_length=155)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2024, 5, 15, 11, 43, 55, 761494))),
                ('update_at', models.DateTimeField(default=datetime.datetime(2024, 5, 15, 11, 43, 55, 761494))),
                ('IR', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_gaulke_contabil_v2.model_tb_imposto_de_renda')),
            ],
        ),
        migrations.CreateModel(
            name='customuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(default='-', max_length=25, null=True)),
                ('sector', models.CharField(max_length=25)),
                ('sessao_atividades', models.BooleanField(default=False)),
                ('sessao_relatorios', models.BooleanField(default=False)),
                ('sessao_imposto_de_renda', models.BooleanField(default=False)),
                ('sessao_config_users', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='custom_user_permissions', to='auth.permission')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
