from django.urls import path
from .views import run_zphisher, show_zphisher_page

urlpatterns = [
    path('', show_zphisher_page, name='show_zphisher_page'),
    path('run-zphisher/', run_zphisher, name='run_zphisher'),
]