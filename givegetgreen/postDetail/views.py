#! /usr/bin/env python2.7
from django.views.generic import TemplateView

class PostDetailView(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        context = {
            'title': 'Give Get Green',
            'some_dynamic_value': 'This text comes from django view!',
        }
        return self.render_to_response(context)