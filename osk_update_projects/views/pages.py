from django.shortcuts import render


def index(request):
    return render(request, 'osk_update_projects/index.html')