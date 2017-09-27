# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from forms import CardForm
from django.views import View
from models import Card

# Create your views here.
class MakeView(View):
    def get(self, request):
        context = {
            'cards': Card.objects.all(),
            'form': CardForm(),
        }
        return render(request, 'cards/index.html', context)

    def post(self, request):
        print('you go there!')
        form = CardForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('card-index')