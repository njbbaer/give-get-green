#! /usr/bin/env python2.7
from django.views.generic import TemplateView

class DeletePostView(TemplateView):
    template_name = 'detailpost.html'

    def post(self, request, *args, **kwargs):
        print "put"
        if request.method == 'POST':
            request_user_name = request.POST.get('request_user_name', '')
            request_user_email = request.POST.get('request_user_email', '')
            request_user_zipcode = request.POST.get('request_user_zipcode', '')
            request_user_phone = request.POST.get('request_user_phone', '')
            request_user_item_id = request.POST.get('request_user_item_id', '')

            context = {
                'title': 'form deleted',
                'request_user_name':request_user_name,
                'request_user_email':request_user_email,
                'request_user_zipcode':request_user_zipcode,
                'request_user_phone':request_user_phone,
                'request_user_item_id':request_user_item_id

            }

        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        context = {
            'title': 'Give Get Green',
            'some_dynamic_value': 'This text comes from django view!',
        }
        return self.render_to_response(context)