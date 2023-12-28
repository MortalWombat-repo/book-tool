# book_tool

**Description of the tool**


**Usage**

book_tool has several commands to help you find book information.

book command:
`book "author" "title"`
Using the command with the author and title helps you find the specific book easier, and by default the language is set to english.

book command also has the option to add the information to the database so you can view the books you are most interested in.
`book "author" "title" "add"`
The database keeps track of various pieces of information such as: title, author, publisher, rating and the number of ratings.

Sometimes very popular books have a lot of editions and it is troublesome trying to find the specific edition if you don't know what you are looking for or aren't looking for an edition with a signifier such as ISBN or a Dewey number.
That is why the book command also has the option to specify the max number of results so you can pinpoint your desired book more easily with specifying the number of results. Due to the nature of the source there can only be a maximum of 40 entries but that is usually more than enough. By default it outputs first ten results.
`book "author" "title" "add" 10`


**Installing Dependencies**

This project uses a number of Python libraries.   
You can install them using the requirements.txt file included in the project's root directory.  

Here's how:  
- Open a terminal window.  
- Navigate to the project's root directory.  
- Run the following command:

```terminal
pip install -r requirements.txt
```

This command tells pip (a package manager for Python) to install all the libraries listed in the requirements.txt file.
