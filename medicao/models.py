# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

from paciente.models import Paciente
from isotopo.models import Isotopo

# TODO
# - defined decimal max_digits, decimal_places
# - PESQUISAR SOBRE STRIPDURATION FORMULA
# - checar sobre HARDCODES

class IndicacaoClinica(models.Model):
	nome = models.CharField(max_length=200)

	def __unicode__(self):
		return nome

class Medicao(models.Model):
	paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
	hora_de_medicao = models.DateTimeField()
	hora_atual = models.DateTimeField()
	hora_de_referencia = models.DateTimeField()
	atividade_inicial_mCi = models.DecimalField(max_digits=5, decimal_places=2)
	isotopo = models.ForeignKey(Isotopo)
	peso = models.DecimalField(max_digits=5, decimal_places=2)
	indicacao_clinica = models.ForeignKey(IndicacaoClinica)
	horario_injecao = models.DateTimeField()
	concentracao_mCi = models.DecimalField(max_digits=5,decimal_places=2,)
	atividade_fracionada = models.DecimalField(max_digits=5, decimal_places=2)
	horario_atividade_fracionada = models.DateTimeField()
	atividade_do_rejeito_da_injecao = models.DecimalField(max_digits=5,decimal_places=2)
	horario_da_atividade_do_rejeito = models.DateTimeField()


	def _atividade_corrigida_do_frasco_mCi(self):
		# = _atividade_do_frasco_descontada x EXPFORMULA((-0.693(HARDCODE) x _delta_tempo_geral) / self.isotopo.hora)
		return
	_atividade_corrigida_do_frasco_mCi = property(_atividade_corrigida_do_frasco_mCi)

	def _atividade_necessaria_total(self):
		# = SOMA_DE_TODAS_MEDICOES(_atividade_necessaria / EXPFORMULA(-0693 x _delta_tempo_at_nec_total / self.isotopo.hora) + (idem_anterior) x concentracao_mCi
		return (self.peso * self.concentracao_mCi)

	def _atividade_necessaria(self):
		# peso x concentracao_mCi
		return (self.peso * self.concentracao_mCi)

	def _delta_tempo_at_nec_total(self):
		# horario_injecao x horario_de_referencia
		# STRIPDURATIONFORMULA(self.horario_injecao - self.horario_de_referencia) x 24 (HARDCODE)
		return

	def _delta_tempo_injecao_rejeito(self):
		# hora (h)
		# STRIPDURATIONFORMULA(horario_da_atividade_rejeito - horario_atividade_fracionada) x 24 (HARDCODE)
		return

	def _atividade_inicial_do_rejeito(self):
		# na hora da injecao
		# = atividade_do_rejeito_da_injecao / EXPFORMULA(-0.693(=HARDCODE) x _delta_tempo_injecao_rejeito / self.isotopo.hora)
		return

	def _ativida_injetada(self):
		# = atividade_fracionada - _atividade_inicial_do_rejeito
		return

	def _delta_tempo(self):
		# STRIPDURATIONFORMULA(horario_atividade_fracionada - horario_da_medicao) x 24 (HARDCODE)
		return

	def _atividade_do_frasco_sem_desconto_da_retirada(self):
		# = atividade_inicial_mCi x EXPFORMULA(-0.693(HARCODE) x _delta_tempo / self.isotopo.hora)
		return

	def _atividade_do_frasco_descontada(self):
		# = _ativida_do_frasco_sem_desconto_da_retirada - atividade_fracionada
		return
