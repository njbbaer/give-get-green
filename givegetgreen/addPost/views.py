#! /usr/bin/env python2.7
from django.views.generic import TemplateView

class AddPostView(TemplateView):
    template_name = 'viewpost.html'

    def post(self, request, *args, **kwargs):
        print "put"
        postdict = dict(request.POST)
        print postdict
        context = ''
        
        if (request.method == 'POST') and ("submit-searchForm" in postdict) :
            context = {'title':'Search results', 'posts':[]}	
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):


        context = {
            'title': 'Give Get Green',
            'some_dynamic_value': 'This text comes from django view!',
        }
        return self.render_to_response(context)
