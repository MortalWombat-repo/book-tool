# book_tool


**Description of the tool**  

A suite of tools to query the book information and keep an organized personal library.

**Usage**  

book_tool has several commands to help you find book information with additional options as well.

**book command:**  
`book "author" "title"`

Using the command with the author and title helps you find the specific book easier,  
by default the language is set to english.

Using the **book** with the option add will add the book to your database.  
It tracks various pieces of information such as: title, author, publisher, rating and the number of ratings.
`book "author" "title" "add"`

Popular books often have different editions and it is difficult to find specific editions without an ISBN or a Dewey number.
Therefore an option to specify the max number of results is also available.
It is limited to 40 entries because of the policy set by the information provider, but oftentimes that is more than enough.
By default without specifying the number yourself the results parameter is set to 10.
`book "author" "title" "add" 10`

**book** command is the most used command. Yet there are additional commands that you may use if you wish to browse.

**title** command searches by the title name of the book. Usually titles have a lots of different editions.
That is why title command also comes with the ability to choose the number of results that are displayed.
The number of results by default is also 10.
`title "Title of the book" 10`

**author** command searches by the books by the name of the author.
author command also comes with the ability to choose the number of results that are displayed.
The number of results by default is also 10.
`author "Author" 10`

**view** command displays book information in your database.
`view`

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
