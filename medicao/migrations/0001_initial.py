# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-11 21:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('isotopo', '0001_initial'),
        ('paciente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndicacaoClinica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Medicao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora_de_medicao', models.DateTimeField()),
                ('hora_atual', models.DateTimeField()),
                ('hora_de_referencia', models.DateTimeField()),
                ('atividade_inicial_mCi', models.DecimalField(decimal_places=2, max_digits=5)),
                ('peso', models.DecimalField(decimal_places=2, max_digits=5)),
                ('horario_injecao', models.DateTimeField()),
                ('concentracao_mCi', models.DecimalField(decimal_places=2, max_digits=5)),
                ('atividade_fracionada', models.DecimalField(decimal_places=2, max_digits=5)),
                ('horario_atividade_fracionada', models.DateTimeField()),
                ('atividade_do_rejeito_da_injecao', models.DecimalField(decimal_places=2, max_digits=5)),
                ('horario_da_atividade_do_rejeito', models.DateTimeField()),
                ('indicacao_clinica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicao.IndicacaoClinica')),
                ('isotopo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='isotopo.Isotopo')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paciente.Paciente')),
            ],
        ),
    ]
