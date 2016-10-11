from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Paciente(models.Model):
	nome = models.CharField(max_length=200)

	def __unicode__(self):
		return self.nome