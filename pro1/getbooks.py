import os, csv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
# engine = create_engine(os.getenv("DATABASE_URL"))                                                 
engine = create_engine(os.getenv("buk1"))                                                 
db = scoped_session(sessionmaker(bind=engine))


#isbn,title,author,year
f = open("books.csv")
reader = csv.reader(f)
for isbn, title, author, year in reader: 
	db.execute("INSERT INTO books (isbn, title, author, year) VALUES				 (:isbn, :title, :author, :year)", {"isbn": isbn, "title": title, "author": author, "year":year })
	print(f"Added book isbn {isbn} title: {title} by {author}.")
db.commit()

