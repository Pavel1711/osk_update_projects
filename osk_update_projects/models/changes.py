from django.db import models
from osk_update_projects.models.version import Version


# =========================================================================================================
# Changes
# =========================================================================================================
class Changes(models.Model):
    text = models.TextField(verbose_name='Изменения', max_length=256)
    version = models.ForeignKey(Version, verbose_name='Версия', on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Изменения'
        verbose_name_plural = 'Изменения'
        ordering = ['id']