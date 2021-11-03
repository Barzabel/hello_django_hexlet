from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect
from django.urls import reverse


class index(View):

    def get(self, request, *args, **kwargs):
        return redirect(reverse('calc', kwargs={'A': 40, 'B': 2}))
