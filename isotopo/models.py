from __future__ import unicode_literals

from django.db import models

# TODO
# - definir tamanho do nome (em caracteres)
# - o que significa o campo min?
# - definir max_digits e decimal_places nos DecimalFields
#

class Isotopo(models.Model):
	nome = models.CharField(max_length=100)
	min = models.DecimalField(max_digits=5,decimal_places=2)
	hora = models.DecimalField(max_digits=5,decimal_places=2)
	formula = models.CharField(max_length=50)

	def __unicode__(self): # __unicode__ on Python 2
		return self.nome
