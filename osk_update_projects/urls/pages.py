from django.urls import path

from osk_update_projects.views.pages import *

urlpatterns = [
    path('', index, name='index')
]
