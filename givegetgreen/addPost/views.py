#! /usr/bin/env python2.7
from django.views.generic import TemplateView
from givegetgreen.posting.models import Posting

class AddPostView(TemplateView):
    template_name = 'viewpost.html'

    def post(self, request, *args, **kwargs):
        print "put"
        postdict = dict(request.POST)
        print postdict
        context = ''
        
	## insert to database by submit giveForm
#        if (request.method == 'POST') and ("submit-giveForm" in postdict) :
#            user_name = request.POST.get('user_name', '')
#            user_email = request.POST.get('user_email', '')
#            user_zipcode = request.POST.get('user_zipcode', '')
#            user_phone = request.POST.get('user_phone', '')
#            user_item_category = request.POST.get('user_item_category', '')
#            user_item = request.POST.get('user_item', '')
#            user_item_description = request.POST.get('user_item_description', '')
#            user_item_id = 1
#
#            posting = Posting(
#                name = user_name,
#                email = user_email,
#                zipcode = user_zipcode,
#                phone = user_phone,
#                item = user_item_category,
#                item_category = user_item_category,
#                item_description = user_item_description
#            )
#            posting.save()
#
#            form_submitted = {
#                'user_name':user_name,
#                'user_email':user_email,
#                'user_zipcode':user_zipcode,
#                'user_phone':user_phone,
#                'user_item_id':user_item_id,
#                'user_item_category': user_item_category,
#                'user_item':user_item,
#                'user_item_description':user_item_description
#            }
#            context = {'title': 'Submitted', 'posts': [form_submitted]}
	## search database by submitting search form
        if (request.method == 'POST') and ("submit-searchForm" in postdict) :
            context = {'title':'Search results', 'posts':[]}	
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):


        context = {
            'title': 'Give Get Green',
            'some_dynamic_value': 'This text comes from django view!',
        }
        return self.render_to_response(context)
