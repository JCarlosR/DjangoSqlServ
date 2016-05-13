from __future__ import unicode_literals

from django.db import models

class Planilla(models.Model):
	idPlanilla = models.IntegerField()
	idAfp = models.CharField(max_length=18)
	idTrabajador= models.CharField(max_length=18)
	idMes = models.CharField(max_length=18)
	DiasFalta = models.CharField(max_length=18)
	HorasFalta = models.CharField(max_length=18)
	TotalIngresos = models.DecimalField(max_digits=7, decimal_places=2)
	TotalDescuentos = models.DecimalField(max_digits=7, decimal_places=2)
