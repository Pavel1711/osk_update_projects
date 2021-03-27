from django.db import models


# =========================================================================================================
# Version
# =========================================================================================================
class Version(models.Model):
    number = models.FloatField(verbose_name='Номер версии')

    def __str__(self):
        return self.number

    def __unicode__(self):
        return self.number

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
        ordering = ['number']