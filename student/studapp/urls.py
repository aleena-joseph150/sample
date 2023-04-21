from django.urls import path
from .views import *
urlpatterns=[
    path('add/',add,name='add'),
    path('view/',view,name='view')

]