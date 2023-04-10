from django.urls import path
from .views import *

urlpatterns = [
    #path('t',TodoView.as_view(), name='todo'),
    path('dep',DepenseCreateView.as_view(),name='dep_c'),
    path('<int:pk>/dep_update',DepenseUpdateView.as_view(),name='dep_up'),
    path('<int:pk>/dep_delete',DepenseDeleteView.as_view(),name='dep_del'),
]