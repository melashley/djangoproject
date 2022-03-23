from django.conf import settings
from django.db import models
from django.utils import timezone


class Compound(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    IUPAC_name = models.TextField()
    CASRN = models.TextField()
    SMILES = models.TextField()
    InChIKey = models.TextField()
    InChI = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.IUPAC_name


class Compound_Data(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    IUPAC_name = models.TextField()
    molecular_weight = models.TextField()
    boiling_point = models.TextField()
    melting_point = models.TextField()
    solubility = models.TextField()
    density = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.IUPAC_name


# Create your models here.
