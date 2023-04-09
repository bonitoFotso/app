from django.urls import path
from .views import *

urlpatterns = [
    #path('t',TodoView.as_view(), name='todo'),
    path('',TodoCreateView.as_view(),name='c'),
    path('<int:todo_id>/update',TodoUpdateView.as_view(),name='u'),
    path('<int:todo_id>/delete',TodoDeleteView.as_view(),name='d'),
]