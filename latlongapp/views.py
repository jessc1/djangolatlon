from django.shortcuts import render
from django.views.generic  import ListView, DetailView, CreateView, \
     UpdateView, DeleteView, TemplateView

#from django.views.generic import TemplateView
from django.urls import reverse_lazy
from .models import Local
from django.db.models import Q


class HomePageView(TemplateView):
    template_name = 'home.html'

class LocalListView(ListView):
    model = Local
    context_object_name = 'local_list'
    template_name = 'local_list.html'
    success_url = reverse_lazy('home.html')


class LocalDetailView(DetailView):
    model = Local
    template_name = 'local_detail.html'


class LocalCreateView(CreateView):
    model = Local
    template_name = 'add_local.html'
    fields = ['name', 'address', 'city',
              'lat', 'lon', 'area','region', 'visited']


class LocalUpdateView(UpdateView):
    model = Local
    template_name= 'update_local.html'
    fields = ['name', 'address', 'city',
              'lat', 'lon', 'area','region', 'visited']

class LocalDeleteView(DeleteView):
    model = Local
    template_name = 'delete_local.html'
    success_url = reverse_lazy('local_list')    

class SearchResultsListView(ListView):
    model = Local
    context_object_name = 'local_list'
    template_name = 'search_local.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Local.objects.filter(
            Q(name__icontains=query)|Q(region__icontains=query)|Q(location__icontains=query)

        )    


