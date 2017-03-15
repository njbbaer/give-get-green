#! /usr/bin/env python2.7
from django.views.generic import TemplateView
from search import search

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
            for result in results:
                post = {
                    'user_item_id': result[0],
                    'user_name': result[1],
                    'user_email': result[2],
                    'user_phonenumber': result[3],
                    'user_address': result[4],
                    'user_item_category': result[5],
                    'user_item_description': result[6],
                    'user_item': result[7],
                }
                posts.append(post)

            context = {'title':'Search results', 'posts':posts}	
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):


        context = {
            'title': 'Give Get Green',
            'some_dynamic_value': 'This text comes from django view!',
        }
        return self.render_to_response(context)
