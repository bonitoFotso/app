from django.shortcuts import render
from django.views.generic import *
from .models import *
from todo.models import *
from finance.models import *
from finance.operation import *

# Create your views here.

class Home(TemplateView):
    template_name = 'home/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["t_all"] = Todo.objects.order_by('-created_at') 
        context['n_t'] = Todo.objects.count()
        context["t_acc"] = Todo.objects.filter(isCompleted = 'True').values().count
        context["depense_list"] = Depense.objects.order_by('-created_at') 
        context["tt"] = ex_total(Depense)
        context['page'] = 'home'
        return context
    