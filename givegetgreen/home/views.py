#! /usr/bin/env python2.7
from django.views.generic import TemplateView
from django.shortcuts import redirect

class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        context = {
            'title': 'Give Get Green',
            'some_dynamic_value': 'This text comes from django view!',
        }
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        print "put"
        context = {
            'title': 'Give Get Green',
            'some_dynamic_value': 'This text comes from django view!',
        }
        postdict = dict(request.POST)
        print postdict
	## insert to database by submit giveForm
        if (request.method == 'POST') and ("submit-giveForm" in postdict) :
            user_name = request.POST.get('user_name', '')
            user_email = request.POST.get('user_email', '')
            user_zipcode = request.POST.get('user_zipcode', '')
            user_phone = request.POST.get('user_phone', '')
            user_item_category = request.POST.get('user_item_category', '')
            user_item = request.POST.get('user_item', '')
            user_item_description = request.POST.get('user_item_description', '')
            user_item_id = 1

            posting = Posting(
                name = user_name,
                email = user_email,
                zipcode = user_zipcode,
                phone = user_phone,
                item = user_item_category,
                item_category = user_item_category,
                item_description = user_item_description
            )
            posting.save()

            return redirect('/home', context);