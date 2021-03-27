from django.contrib import admin
from osk_update_projects.models import *


class ChangesAdmin(admin.ModelAdmin):
    base_model = Changes

admin.site.register(Changes, ChangesAdmin)


class ProjectsAdmin(admin.ModelAdmin):
    base_model = Projects

admin.site.register(Projects, ProjectsAdmin)


class VersionAdmin(admin.ModelAdmin):
    base_model = Version

admin.site.register(Version, VersionAdmin)