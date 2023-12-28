import helper
import typer # an alternative to import sys, argparse
import yagmail #simpler alternative to smtplib
import requests #it is almost always better to render directly from url, this is for debugging
import json
from spellchecker import SpellChecker
import nltk
from nltk.tokenize import sent_tokenize
nltk.download('punkt')
from typing_extensions import Annotated
from tabulate import tabulate
import textwrap
from typing import Optional
import sqlite3

spell = SpellChecker(language='en')
#initialize a typer object to later be used with decorator command 
app = typer.Typer()

# command that searches for articles resembling the input
@app.command()
def book(title: str, author: str, action: Annotated[Optional[str], typer.Argument()] = None, results: Annotated[Optional[int], typer.Argument()] = 10):
    response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q=intitle:{title}+inauthor:{author}&maxResults={results}")
    data = response.json()
    title = data['items'][0]['volumeInfo']['title']
    authors = data['items'][0]['volumeInfo']['authors']
    description =  data['items'][0]['volumeInfo']['description']
    sentences = sent_tokenize(description)
    sentences = '\n'.join(sentences)
    rating = data['items'][0]['volumeInfo']['averageRating']
    ratingcount = data['items'][0]['volumeInfo']['ratingsCount']
    data = {'title': title, 'authors': authors, 'sentences': sentences, 'rating': rating, 'ratingcount': ratingcount}
    for key, value in data.items():
        typer.echo(f"{key}: {value}")

    if action == "add":
        # Create a connection to your database
        conn = sqlite3.connect('my_book.db')

        # Create a cursor object
        cur = conn.cursor()
        
        cur.execute("""
        CREATE TABLE IF NOT EXISTS "my_book" (
            id INTEGER PRIMARY KEY,
            title TEXT,
            author TEXT,
            sentences TEXT,
            rating INTEGER,
            rating_count INTEGER
        )
            """)
        # Execute the INSERT INTO statement
        cur.execute("INSERT INTO my_book (title, author, sentences, rating, rating_count) VALUES (?, ?, ?, ?, ?)", 
                    (title, author, sentences, rating, ratingcount))

        # Commit the changes and close the connection
        conn.commit()
        conn.close()


@app.command()
def title(title: str, results: Annotated[Optional[int], typer.Argument()] = 10):
    response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q=intitle:{title}&maxResults={results}")
    data = response.json()
    titles = []
    if data.get("items"):
        for item in data["items"]:
            book_title = item["volumeInfo"].get("title", "No title available")
            book_author = item["volumeInfo"].get("authors", "No author available")
            book_publish = item["volumeInfo"].get("publisher", "No publisher available")
            titles.append((book_title, book_author, book_publish))
    for i, item in enumerate(titles, start=1):
        typer.echo(f"{i}. Title: {item[0]}, Author: {', '.join(item[1])}, Publisher: {item[2]}")

@app.command()
def author(author: str, results: Annotated[Optional[int], typer.Argument()] = 10):
    response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q=intitle:{author}&maxResults={results}")
    data = response.json()
    titles = []
    if data.get("items"):
        for item in data["items"]:
            book_title = item["volumeInfo"].get("title", "No title available")
            book_author = item["volumeInfo"].get("authors", "No author available")
            book_publish = item["volumeInfo"].get("publisher", "No publisher available")
            titles.append((book_title, book_author, book_publish))
    for i, item in enumerate(titles, start=1):
        typer.echo(f"{i}. Author: {', '.join(item[1])}, Title: {item[0]}, Publisher: {item[2]}")
    
@app.command()
def view():
    # Create a connection to your database
    conn = sqlite3.connect('my_book.db')

    # Create a cursor object
    cur = conn.cursor()
    
    cur.execute("""
    CREATE TABLE IF NOT EXISTS "my_book" (
        id INTEGER PRIMARY KEY,
        title TEXT,
        author TEXT,
        sentences TEXT,
        rating INTEGER,
        rating_count INTEGER
    )
        """)
    # Execute the INSERT INTO statement
    cur.execute("SELECT * FROM my_book")

    rows = cur.fetchall()
    # Wrap text to 50 characters
    wrapped_rows = []
    for row in rows:
        wrapped_row = [textwrap.fill(str(item)[:35], width=10) if i == 3 else textwrap.fill(str(item), width=10) for i, item in enumerate(row)]
        wrapped_rows.append(wrapped_row)
    print(tabulate(wrapped_rows))

    conn.close()