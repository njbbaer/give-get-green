import sqlite3
from whoosh.index import create_in
from whoosh.fields import *
from whoosh.qparser import QueryParser
from whoosh import sorting
import os.path
import shutil
from whoosh.index import open_dir


# CREATING AN INDEX OF DATABASE
if not os.path.exists("indexdir"):
	os.mkdir("indexdir")	
conn=sqlite3.connect('example.db');
c=conn.cursor();
schema = Schema(title=TEXT(stored=True),description=TEXT(stored=True),category=TEXT(stored=True),name=STORED, zipcode=STORED,phone=STORED,email=STORED)
ix = create_in("indexdir", schema)
writer = ix.writer()
for row in c.execute('SELECT title,description,category,name,zipcode,phone,email FROM DB_GGG'):
	writer.add_document(title=row[0], description=row[1], category=row[2], name=row[3], zipcode=row[4], phone=row[5], email=row[6])
	print row
writer.commit()
