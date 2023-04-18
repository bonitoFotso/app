from django.shortcuts import render
from django.views.generic import *
from django.urls import reverse_lazy
from .models import *
from .operation import total
# Create your views here.


class DepenseCreateView(CreateView):
    model = Depense
    fields = ['title', 'montant']
    template_name = 'depense/depense.html'        
    success_url =reverse_lazy('dep_c')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["depense_list"] = self.model.objects.order_by('-created_at') 
        context["tt"] = total(self)
        context['num'] = self.model.objects.count()
        context['page'] = 'depense'
        return context
    
class DepenseDeleteView(DeleteView):
    model = Depense
    template_name = 'depense/depense.html'
    success_url =reverse_lazy('dep_c')
    
class DepenseUpdateView(UpdateView):
    model = Depense
    fields = ['title', 'montant']
    template_name = 'depense/depense.html'
    success_url =reverse_lazy('dep_c')
    
    