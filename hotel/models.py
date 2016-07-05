from django.db import models

# Create your models here.


class zimmer(models.Model):
	zimmer_id = models.AutoField(primary_key=True)
	zimmer = models.TextField('Zimmername')
	preis = models.IntegerField('Zimmerpreis in Euro pro Nacht')
	#status = models.IntegerField('Buchbar?')
	status = models.CharField(max_length=4, choices= ((u'ja', u'Buchbar',), (u'nein', u'nicht Buchbar')))
	max_betten = models.IntegerField('Anzahl max. Betten')
	image = models.ImageField(upload_to = 'static/images/')
	def __str__(self):
		return "%s %s" % (self.zimmer_id, self.zimmer)



class buchung(models.Model):
	#zimmer_id =  models.IntegerField('Zimmernummer')
	#zimmer_id = models.CharField(max_length=4, choices= (u'zimmer.objects.id','test'))
	zimmer_id = models.ForeignKey(zimmer, on_delete=models.CASCADE)
	nutzer = models.TextField('Nutzername')
	#nutzer = models.ForeignKey(kunden, on_delete=models.CASCADE)
	#nutzer = models.ManyToManyField(vorname)
	anzahl_tage = models.IntegerField('Anzahl der zu buchenden Tage')
	datum_von = models.DateField()
	datum_bis = models.DateField()
	zimmer_objekte = zimmer()
	def __str__(self):
		return "Gebucht wurde Zimmer '{}'von '{}'".format(self.zimmer_id,self.nutzer)


class kunden(models.Model):
	#kunden_id = models.IntegerField('Kunden')
	vorname = models.TextField('Vorname')
	nachname =  models.TextField('Nachname')
	#zimmer = models.IntegerField('Zimmernummer')
	zimmer =  models.ForeignKey(zimmer, on_delete=models.CASCADE)
	aktiv =  models.CharField(max_length=4, choices= ((u'1', u'Eingecheckt',), (u'0', u'nicht Eingecheckt')))
	def __str__(self):
		return "Der Kunde '{}' '{}' hat zur Zeit folgendes Zimmer gebucht '{}' ".format(self.vorname,self.nachname,self.zimmer)
