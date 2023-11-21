from specific.views import *
from django.urls import path

app_name='challenger'

urlpatterns=[

    path('speedy/',speedy,name='speedy'),
    path('spidy/',spidy,name='spidy'),
    
]