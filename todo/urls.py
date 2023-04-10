from django.urls import path
from .views import *

urlpatterns = [
    #path('t',TodoView.as_view(), name='todo'),
    path('',TodoCreateView.as_view(),name='c'),
    path('<int:pk>/update',TodoUpdateView.as_view(),name='u'),
    path('<int:pk>/delete',TodoDeleteView.as_view(),name='d'),
]