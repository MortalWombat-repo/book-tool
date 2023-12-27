from pyfiglet import Figlet
from tabulate import tabulate
import typer

def figlet():
    f = Figlet(font='small', width = 200)
    print(f.renderText('book tool'))

def top():
    text_top = """
Usage:
    book- [Name of the book]
    author- [Name of the author]
    genre- [Name of the genre]
    list_genre [List all available_genres]
    random_book [Suggest a random book]
    random_author [Suggest a random author]
    add book- [Add book to the reading list]
    set_book [Set book as reading, read or planning to read]"""
    
    table = [[text_top]]
    top = tabulate(table, tablefmt='grid')
    print(top)
