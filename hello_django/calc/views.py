from django.http import HttpResponse
from django.views.generic.base import TemplateView

class index(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        res = str(kwargs['A'] + kwargs['B'])
        context = super().get_context_data(**kwargs)
        context['val'] = '{} + {} = {}'.format(kwargs['A'], kwargs['B'], res)
        return context

