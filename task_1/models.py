from django.db import models


class AutoShow(models.Model):
    email = models.EmailField(max_length=128, db_index=True, verbose_name="Почта")
    motor = models.IntegerField(verbose_name="Мощность двигателя")
    date_birth = models.DateField(verbose_name="Дата рождения")
    brand = models.CharField(max_length=128, verbose_name="Марка")



class Appointment(models.Model):
    title_appoint = models.CharField(max_length=128, verbose_name="Назначение")
    appointment = models.ForeignKey(
        'AutoShow',
        on_delete=models.CASCADE,
        verbose_name="appoint_auto_id"
    )

class Provider(models.Model):
    title_provider = models.CharField(max_length=128, verbose_name="Постовщик")
    provider = models.ForeignKey(
        'AutoShow',
        on_delete=models.CASCADE,
        verbose_name="provider_auto_id"
    )