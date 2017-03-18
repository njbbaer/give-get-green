#! /usr/bin/env python2.7
from django.views.generic import TemplateView
from search import search
from givegetgreen.posting.models import Posting

class AddPostView(TemplateView):
    template_name = 'viewpost.html'

    def post(self, request, *args, **kwargs):
        print "put"
        postdict = dict(request.POST)
        print postdict
        context = ''
        
        if (request.method == 'POST') and ("submit-searchForm" in postdict) :
            search_item = request.POST.get('search_item', '')
            category = request.POST.get('item_category', '')
            distance = int(request.POST.get('distance', ''))
            address = request.POST.get('user_address', '')

            query = category + " " + search_item
            results = search.query_result(address, query, distance)

            posts = []
            if results is not None:
                for result in results:
                    post_db = Posting.objects.get(pk=result)
                    post_dict = {
                        'user_item_id': post_db.id,
                        'user_name': post_db.name,
                        'user_email': post_db.email,
                        'user_phonenumber': post_db.phone,
                        'user_address': post_db.address,
                        'user_item_category': post_db.category,
                        'user_item_description': post_db.description,
                        'user_item': post_db.title,
                    }
                    posts.append(post_dict)

            context = {'title':'Search results', 'posts':posts}	
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):


        context = {
            'title': 'Give Get Green',
            'some_dynamic_value': 'This text comes from django view!',
        }
        return self.render_to_response(context)
