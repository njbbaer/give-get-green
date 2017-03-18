#! /usr/bin/env python2.7
from django.views.generic import TemplateView
from django.shortcuts import redirect
from givegetgreen.posting.models import Posting

class DeletePostView(TemplateView):
    template_name = 'detailpost.html'

    def post(self, request, *args, **kwargs):
        print "put"
        if request.method == 'POST':
            request_user_item_id = request.POST.get('request_user_item_id', '')

            Posting.objects.filter(id=request_user_item_id).delete()

            context = {
                'title': 'form deleted',
                'request_user_item_id':request_user_item_id

            }

        return redirect('/home', context);

    def get(self, request, *args, **kwargs):
        context = {
            'title': 'Give Get Green',
            'some_dynamic_value': 'This text comes from django view!',
        }
        return self.render_to_response(context)