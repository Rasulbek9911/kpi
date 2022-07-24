from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView
from django.views.generic.edit import BaseCreateView
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from . import models
from . import forms


class IndexView(TemplateView):
    template_name = 'index.html'


class XodimCreateView(CreateView):
    template_name = 'xodim.html'
    model = models.Xodim
    fields = ['type_doc', 'description', 'file']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class MyDocListView(ListView):
    template_name = 'myDoc.html'
    context_object_name = 'docs'
    form_class = forms.XodimForm

    def get_queryset(self):
        queryset = models.Xodim.objects.filter(user=self.request.user, status='0')
        return queryset


class CheckedDocListView(ListView):
    model = models.Xodim
    template_name = 'checkedDoc.html'

    def get_queryset(self):
        queryset = models.Xodim.objects.filter(user=self.request.user, status='1').order_by('-submit_date')
        return queryset


class EditDocDetailView(UpdateView):
    model = models.Xodim
    fields = ('type_doc', 'comment', 'file')
    template_name = 'editDetailDoc.html'
    success_url = "#"


class ArchiveDocDetailView(DetailView):
    template_name = 'archiveDoc.html'

    def get_queryset(self):
        queryset = models.Xodim.objects.filter(user=self.request.user)
        return queryset


def LoginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:

            login(request, user)
            res = redirect('/xodim/')
            return res
        else:
            messages.error(request, "Login yoki parol xato")
    return render(request, 'index.html')


def logout_view(request):
    logout(request)
    return redirect('index')
