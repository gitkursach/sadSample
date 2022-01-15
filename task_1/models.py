from django.contrib.postgres.fields import ArrayField
from django.db import models


class AutoShow_v2(models.Model):
    email = models.EmailField(max_length=128, db_index=True, verbose_name="Почта")
    motor = models.IntegerField(verbose_name="Мощность двигателя")
    date_birth = models.DateField(verbose_name="Дата рождения")
    brand = models.CharField(max_length=128, verbose_name="Марка")
    appointment = ArrayField(ArrayField(models.CharField(max_length=16, blank=True)))
    provider = ArrayField(ArrayField(models.CharField(max_length=16, blank=True)))


class AutoShow_v3(models.Model):
    email = models.EmailField(max_length=128, db_index=True, verbose_name="Почта")
    motor = models.IntegerField(verbose_name="Мощность двигателя")
    date_birth = models.DateField(verbose_name="Дата рождения")
    brand = models.CharField(max_length=128, verbose_name="Марка")
    Appointment = models.CharField(max_length=16, blank=True)
    provider = models.CharField(max_length=16, blank=True)
