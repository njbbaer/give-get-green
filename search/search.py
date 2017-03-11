import sqlite3
from whoosh.index import create_in
from whoosh.fields import *
from whoosh.qparser import QueryParser
from whoosh import sorting
import os.path
import shutil
from whoosh.index import open_dir
from whoosh.query import *
from whoosh.qparser import MultifieldParser


# CREATING A DATABASE
def create_database():
	if os.path.exists("givegetgreen_db"):
		os.remove("givegetgreen_db")
	if not os.path.exists("givegetgreen_db"):
		conn=sqlite3.connect('givegetgreen_db');
		c=conn.cursor();
		c.execute('''CREATE TABLE posting_posting (title text, description text, category text, name text, zipcode text, phone text, email text)''');
		c.execute('''INSERT INTO posting_posting VALUES ('mobile','in very good condition','electronics','a','92612','9495995959','a@uci.edu')''');
		c.execute('''INSERT INTO posting_posting VALUES ('tv','10 years old','electronics','b','92613','9495995950','b@uci.edu')''');
		c.execute('''INSERT INTO posting_posting VALUES ('radio','latest latest 1987 classic collection','electronics','a','92614','9495995951','c@uci.edu')''');
		c.execute('''INSERT INTO posting_posting VALUES ('bottle','plastic bottles 12','recyclable','b','92615','9495995952','d@uci.edu')''');
		c.execute('''INSERT INTO posting_posting VALUES ('jeans','blue denim latest style','clothes','a','92616','9495995953','e@uci.edu')''');
		c.execute('''INSERT INTO posting_posting VALUES ('chair','wooden blue wooden blue 2 latest latest latest latest latest','furniture','b','92617','9495995954','f@uci.edu')''');
		c.execute('''INSERT INTO posting_posting VALUES ('pot','very large but still weightless','household','g','92623','9495995959','g@uci.edu')''');
		c.execute('''INSERT INTO posting_posting VALUES ('camera','2 years old in very good condition','electronics','h','92633','9495994550','h@uci.edu')''');
		c.execute('''INSERT INTO posting_posting VALUES ('table','plastic white new','furniture','i','92644','9495995951','i@uci.edu')''');
		c.execute('''INSERT INTO posting_posting VALUES ('matress','queen size white soft latest','household','j','92655','9495954952','j@uci.edu')''');
		c.execute('''INSERT INTO posting_posting VALUES ('shirts','jean wooden blue white red gree palo','clothes','k','92666','9495235953','k@uci.edu')''');
		c.execute('''INSERT INTO posting_posting VALUES ('pants','3 denim shades of blue latest','clothes','l','92677','9495945454','l@uci.edu')''');
		for row in c.execute('SELECT * FROM posting_posting'):
			print row
		conn.commit()
		conn.close()


# CREATING AN INDEX OF DATABASE
def create_index(indexdir,database_name):
	if not os.path.exists(indexdir):
		os.mkdir("indexdir")	
	conn=sqlite3.connect(database_name);
	c=conn.cursor();
	schema = Schema(title=TEXT(stored=True),description=TEXT(stored=True),category=TEXT(stored=True),name=STORED, zipcode=STORED,phone=STORED,email=STORED)
	ix = create_in(indexdir, schema)
	writer = ix.writer()
	for row in c.execute('SELECT title,description,category,name,zipcode,phone,email FROM posting_posting'):
		writer.add_document(title=row[0], description=row[1], category=row[2], name=row[3], zipcode=row[4], phone=row[5], email=row[6])
		# print row
	writer.commit()


# PARSE A QUERY STRING AND SEARCH RESULTS IN SORTED ORDER
def query_result(search_query):
	hits=[]
	d={}
	ix=open_dir("indexdir")
	f=open("search_results.txt","a")
	query=""
	search_list= search_query.split(" ")
	for words in search_list:
		query= str(query) + str(words) + " OR "
	query=query+" "
	search_query=query
	print search_query		
	with ix.searcher() as searcher:
		query = MultifieldParser(["title", "description"], schema=ix.schema).parse(search_query)
    	# query = QueryParser("description" AND "title", ix.schema).parse(u'latest')
		results = searcher.search(query)
		# print results[0]
		for words in results:
			f.write(str(words)+"\n")
			hits.append(str(words))
			print words.score, words
	return hits		


# MAIN FUNCTION
if __name__=="__main__":

	create_database()

	# assign database_name as desired
	indexdir="indexdir"
	database_name="givegetgreen_db"
	create_index(indexdir,database_name)

	# assign search_query as entered by the user 
	# hits contains the top search results sorted
	search_query='jean wooden'
	hits=query_result(search_query)
	print hits