import sqlite3
from whoosh.index import create_in
from whoosh.fields import *
from whoosh.qparser import QueryParser
from whoosh import sorting
import os.path
from whoosh.index import open_dir
from whoosh.query import *
from whoosh.qparser import MultifieldParser

# PARSE A QUERY STRING AND SEARCH RESULTS IN SORTED ORDER
ix=open_dir("indexdir")
f=open("search_results.txt","a")
with ix.searcher() as searcher:
	query = MultifieldParser(["title", "description"], schema=ix.schema).parse(u'latest')
    # query = QueryParser("description" AND "title", ix.schema).parse(u'latest')
	results = searcher.search(query)
	print results[0]
	for words in results:
		f.write(str(words)+"\n")


