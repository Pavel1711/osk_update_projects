from django.db import models
from osk_update_projects.models.version import Version


# =========================================================================================================
# Projects
# =========================================================================================================
class Projects(models.Model):
    name = models.CharField(verbose_name='Наименование портала', max_length=64)
    version = models.ForeignKey(Version, verbose_name='Номер версии', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Проекты'
        verbose_name_plural = 'Проекты'
        ordering = ['name']