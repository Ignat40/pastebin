from dataclasses import fields
import imp
from multiprocessing import context
from pyexpat import model
from re import template
from django.shortcuts import render
from .models import Paste
from django.views import generic


class PasteList(generic.ListView):
    model = Paste
    context_object_name = 'pastes' 



class PasteCreate(generic.edit.CreateView):
    model = Paste
    fields = ['name', 'text']


class PasteDetail(generic.detail.DetailView):
    model = Paste
    template_name = 'pastebin_app/paste_detail.html'

class PasteUpdate(generic.edit.UpdateView):
    model: Paste
    fields = ['name', 'text']

class PasteDelete(generic.DateView):
    model = Paste