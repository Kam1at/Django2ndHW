from django.urls import path
from ormnew.views import control
from ormnew.apps import OrmnewConfig

app_name = OrmnewConfig.name

urlpatterns = [
    path('', control)
]