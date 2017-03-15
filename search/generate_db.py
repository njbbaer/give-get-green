from random_words import RandomWords
from faker import Factory
import random
import sqlite3

NUM_GENERATE = 100

CATEGORIES = ['miscellaneous', 'appliance', 'bedding', 'toys', 'books', 'clothing',
	'seasonal', 'electronics', 'household', 'kitchen', 'sports']

def generate_postings(count):
	postings = []
	for i in range(count):
		faker = Factory.create()
		rw = RandomWords()

		posting = {
			'name': faker.name(),
			'address': faker.city() + ", " + faker.state(),
			'email': faker.email(),
			'phone': random.randint(1000000000, 9999999999),
			'title': " ".join(rw.random_words(count=random.randint(1, 3))),
			'description': " ".join(rw.random_words(count=random.randint(3, 9))),
			'category': random.choice(CATEGORIES),
		}
		postings.append(posting)
	return postings


def write_database(postings):
	conn=sqlite3.connect('givegetgreen_db');
	c=conn.cursor()
	for post in postings:
		# name email phone address category description title
		c.execute('''INSERT INTO posting_posting VALUES (null, '%s', '%s', '%s', '%s', '%s', '%s', '%s')'''
			% (post['name'], post['email'], post['phone'], post['address'], post['category'], post['description'], post['title']));
	conn.commit()
	conn.close()
	print str(len(postings)) + " postings written to database"


if __name__ == '__main__':

	postings = generate_postings(NUM_GENERATE)
	write_database(postings)