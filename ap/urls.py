from django.urls import path
from .views import *

urlpatterns =[
    path('blog/',blog,name='blog'),
    path('blog/<str:name>/detail',detail,name='detail'),
]   