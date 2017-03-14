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
from geopy.geocoders import Nominatim
from geopy.distance import vincenty
from geopy.distance import great_circle
from stemming.porter2 import stem
from nltk import PorterStemmer

# CREATING A DATABASE
def populate_database():
	conn=sqlite3.connect('givegetgreen_db');
	c=conn.cursor();
	c.execute('''INSERT INTO posting_posting VALUES (null, 'mobiles','in very good condition','electronics','a','3800 parkview lane irvine','9495995959','a@uci.edu')''');
	c.execute('''INSERT INTO posting_posting VALUES (null, 'tv','10 years old','electronics','b','3801 parkview lane irvine','9495995950','b@uci.edu')''');
	c.execute('''INSERT INTO posting_posting VALUES (null, 'radio','latest latest 1987 classic collection','electronics','a','university of california irvine','9495995951','c@uci.edu')''');
	c.execute('''INSERT INTO posting_posting VALUES (null, 'bottle','plastic bottles 12','recyclable','b','harvard court irvine','9495995952','d@uci.edu')''');
	c.execute('''INSERT INTO posting_posting VALUES (null, 'jeans','blue denim latest style','clothes','a','stanford court irvine','9495995953','e@uci.edu')''');
	c.execute('''INSERT INTO posting_posting VALUES (null, 'chair','wooden blue wooden blue 2 latest latest latest latest latest','furniture','b','barranca irvine','9495995954','f@uci.edu')''');
	c.execute('''INSERT INTO posting_posting VALUES (null, 'pot','very large but still weightless','household','g','2512 walnut avenue tustin','9495995959','g@uci.edu')''');
	c.execute('''INSERT INTO posting_posting VALUES (null, 'camera','2 years old in very good condition','electronics','h','3901 parkview ln','9495994550','h@uci.edu')''');
	c.execute('''INSERT INTO posting_posting VALUES (null, 'table','plastic white new','furniture','i','university center irvine','9495995951','i@uci.edu')''');
	c.execute('''INSERT INTO posting_posting VALUES (null, 'matress','queen size white soft latest','household','j','berkley avenue irvine','9495954952','j@uci.edu')''');
	c.execute('''INSERT INTO posting_posting VALUES (null, 'shirts','jean wooden blue white red green palo','clothes','k',' 18601 Airport Way, Santa Ana, CA 92707','9495235953','k@uci.edu')''');
	c.execute('''INSERT INTO posting_posting VALUES (null, 'pants','3 denim shades of blue latest','clothes','l','3601 parkview lane irvine','9495945454','l@uci.edu')''');
	conn.commit()
	conn.close()
	print "Database created"


# CREATING AN INDEX OF DATABASE
def create_index(indexdir,database_name):
	if not os.path.exists(indexdir):
		os.mkdir(indexdir)	
	conn=sqlite3.connect(database_name);
	c=conn.cursor();
	schema = Schema(id=NUMERIC(stored=True),title=TEXT(stored=True),description=TEXT(stored=True),category=TEXT(stored=True),name=STORED, address=STORED,phone=STORED,email=STORED)
	ix = create_in(indexdir, schema)
	writer = ix.writer()
	for row in c.execute('SELECT id,title,description,category,name,address,phone,email FROM posting_posting'):
		d1=" "
		d2=" "
		d3=" "
		x1=row[1].split(" ")
		for words in x1:
			d1=d1 + PorterStemmer().stem(words.lower()) + " "
		x2=row[2].split(" ")
		for words in x2:
			d2=d2 + PorterStemmer().stem(words.lower()) + " "
		x3=row[3].split(" ")
		for words in x3:
			d3=d3 + PorterStemmer().stem(words.lower()) + " "
		writer.add_document(id=row[0],title=d1, description=d2, category=d3, name=(row[4].lower()), address=(row[5].lower()), phone=(row[6].lower()), email=(row[7].lower()))
		# print row
	writer.commit()
	print "index created"


# PARSE A QUERY STRING AND SEARCH RESULTS IN SORTED ORDER
def query_result(getter_address, search_query):

	database_name="givegetgreen_db"
	conn=sqlite3.connect(database_name);

	address_list=[]
	all_fields_list=[]
	hits=[]
	d={}
	ix=open_dir("indexdir")
	f=open("search_results.txt","a")

	query=""
	search_list= search_query.split(" ")
	for words in search_list:
		words=PorterStemmer().stem(words.lower())
		query= str(query) + str(words) + " OR "
	query=query+" "
	search_query=query
	# print search_query		
	with ix.searcher() as searcher:
		query = MultifieldParser(["title","category","description"], schema=ix.schema).parse(search_query)
    	# query = QueryParser("description" AND "title", ix.schema).parse(u'latest')
		results = searcher.search(query)
		# print results
		for words in results:
			f.write(str(words)+"\n")
			hits.append(str(words))
			# print words.score, words['address']
			address_list.append(words['address'])

			c=conn.cursor();
			x=int(words['id'])
			x=(x,)
			# print x
			for row in c.execute('SELECT * FROM posting_posting where id= ? ',x ):
				all_fields_list.append(row);
	getter_address= (getter_address.lower())
	conn.commit()
	conn.close()
	return add_filter(getter_address, address_list, all_fields_list)


# FILTER THE RESULTS ACOORDING TO THE ADDRESS
def add_filter(getter_address, address_list, all_fields_list):
	distances=[]
	final_list=[]
	final_all_fields_list=[]
	geolocator = Nominatim()		
	location1 = geolocator.geocode(str(getter_address))
	if len(location1)==0:
		pass
	location1_ll = (location1.latitude, location1.longitude)
	# print len(address_list)
	for i in range(0,len(address_list)):
		# print words
		try:
			words=address_list[i]
			# print (words)
			location2 = geolocator.geocode(str(words))
			location2_ll = (location2.latitude, location2.longitude)
			# print "in"
			distance=(vincenty(location1_ll, location2_ll).miles)
			if distance<=25:
				# print words, distance
				final_list.append(words)
				final_all_fields_list.append(all_fields_list[i])
		except Exception as e :
			print e
			continue
	return final_all_fields_list
			

# MAIN FUNCTION
if __name__=="__main__":

	create_database()

	# assign database_name as desired
	indexdir="indexdir"
	database_name="givegetgreen_db"
	create_index(indexdir,database_name)

	# assign search_query as entered by the user 
	# hits contains the top search results sorted by relevance and filtered by zipcode
	# hit is the tuple.. use this to display results on web page
	search_query='latest'
	getter_address="3801 parkview lane irvine"
	hits=query_result(getter_address, search_query)
	for hit in hits:
		print (hit)
