from django.shortcuts import render
from django.views.generic import *
from django.urls import reverse_lazy
from .models import *
# Create your views here.

#class TodoView(TemplateView,CreateView):
#    #def get(self,request,*args, **kwargs):    
#    template_name = 'todo/todo.html'
#    fields = ['title']
#    #context_object_name = 'todo_list'
#    #def get_context_data(self, **kwargs):
#    #    context = super().get_context_data(**kwargs)
#    #    context["todo_list"] = Todo.objects.order_by('-created_at')
#    #    return context
#    #
#        #return render(request,template_name)
#
#    def get_queryset(self):
#        """Return all the latest todos."""
#        return  Todo.objects.order_by('-created_at')
#   
class TodoCreateView(CreateView):
    model = Todo
    fields = ['title']
    template_name = 'todo/todo.html'
    success_url =reverse_lazy('c')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todo_list"] = Todo.objects.order_by('-created_at') 
        context["tt"] = Todo.objects.filter(isCompleted = 'True').values().count
        context['num'] = Todo.objects.count()
        return context
    
class TodoDeleteView(DeleteView):
    model = Todo
    fields = ['title']
    template_name = 'todo/todo.html'
    success_url =reverse_lazy('c')
    
class TodoUpdateView(UpdateView):
    model = Todo
    fields = ['isCompleted']
    template_name_suffix = 'todo/todo.html'
    success_url =reverse_lazy('c')
    
    