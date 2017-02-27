#! /usr/bin/env python2.7
from django.views.generic import TemplateView

class AddPostView(TemplateView):
    template_name = 'viewpost.html'

    def post(self, request, *args, **kwargs):
        print "put"
        if request.method == 'POST':
            user_name = request.POST.get('user_name', '')
            user_email = request.POST.get('user_email', '')
            user_zipcode = request.POST.get('user_zipcode', '')
            user_phone = request.POST.get('user_phone', '')
            user_item = request.POST.get('user_item', '')
            user_item_description = request.POST.get('user_item_description', '')

            form_submitted = {
                'title': 'form submitted',
                'user_name':user_name,
                'user_email':user_email,
                'user_zipcode':user_zipcode,
                'user_phone':user_phone,
                'user_item':user_item,
                'user_item_description':user_item_description
            }
            context = {'posts': [form_submitted]}
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        print "get"

        context = {
            'title': 'Give Get Green',
            'some_dynamic_value': 'This text comes from django view!',
        }
        return self.render_to_response(context)