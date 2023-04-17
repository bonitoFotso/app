from django.urls import path
from .views import *

urlpatterns = [
    #path('t',TodoView.as_view(), name='todo'),
    path('todo',TodoCreateView.as_view(),name='todo'),
    path('<int:pk>/update',TodoUpdateView.as_view(),name='todo_up'),
    path('<int:pk>/delete',TodoDeleteView.as_view(),name='todo_del'),
]
