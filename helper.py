from pyfiglet import Figlet
from tabulate import tabulate
import typer

def figlet():
    f = Figlet(font='small', width = 200)
    print(f.renderText('book tool'))

def top():
    text_top = """
Usage:
    book- [Name of the book] it needs a book name and an author to be precise
        book "author" "title"

        there is additional option "add"
        book "author" "title" "add" - adds the information to the database

        there is an additional option to customize the number of results.
        by default the number is 10 but it can be set to max 40
        book "author" "title" 20

    title - [Title of the book] this just needs a title. Be wary there are multiple editions
        this is only to remind yourself and browse.
        title "title"

        by default the number is 10 but it can be set to max 40
        book "author" "title" 20

    author - [Author of the book] same situation as title
        author "author"

        by default the number is 10 but it can be set to max 40
        book "author" "title" 20
        
    view - [View your current book database] - a shorter way to view your book database"""
    
    table = [[text_top]]
    top = tabulate(table, tablefmt='grid')
    print(top)
