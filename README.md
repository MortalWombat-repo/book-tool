# book_tool

## Description of the tool

A suite of tools to query the book information and keep an organized personal library.

## Usage

book_tool has several commands to help you find book information with additional options as well.
Available commands: book, title, author, view

**book command:**  
```terminal
book "author" "title"
```

Using the command with the author and title helps you find the specific book easier,  
by default the language is set to english.

Using the **book** with the option add will add the book to your database.  
It tracks various pieces of information   
such as: title, author, publisher, rating and the number of ratings.  
```terminal
book "author" "title" "add"
```

Popular books often have different editions and it is difficult   
to find specific editions without an ISBN or a Dewey number.
Therefore an option to specify the max number of results is also available.
It is limited to 40 entries because of the policy set by the information provider,   
but oftentimes that is more than enough.
By default without specifying the number yourself the results parameter is set to 10.  
```terminal
book "author" "title" "add" 10
```

**book** command is the most used command.  
Yet there are additional commands that you may use if you wish to browse  
and try to search without having a specific book in mind.

**title** command searches by the title name of the book. Usually titles have a lots of different editions.
That is why title command also comes with the ability to choose the number of results that are displayed.
The number of results by default is also 10.  
```terminal
title "Title of the book" 10
```

**author** command searches by the books by the name of the author.
author command also comes with the ability to choose the number of results that are displayed.
The number of results by default is also 10.  
```terminal
author "Author" 10
```

**view** command displays book information in your database.  
```terminal
view
```

## Installing Dependencies

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

Python language comes with the sqlite3 preinstalled, it can only output the information,  
you may not access it yourself in the terminal.

To edit information yourself you would need to install sqlite binaries from:
https://www.sqlite.org/download.html
Important notice sqlite3 does not come with the Python version only with Windows.
If you are runinng MacOS you need to follow the next step.
Even though Mac comes with sqlite3 preinstalled it is advisable to update it to eliminate potential issues.

**for MacOS**

To install SQLite3 on macOS it is easiest using Homebrew.
To install Homebrew paste into your terminal the following command:
```terminal
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Next install SQLite3:
```terminal
brew install sqlite3
```

**Windows**  

To install Sqlite3 in windows visit
https://www.sqlite.org/download.html

If your Windows version is 32 bit follow this guide:
https://stackoverflow.com/a/75627861/22570293

If you have Windows 64 bit:
install sqlite-tools-win-x64-3440200.zip
unzip it and add contents to a high level directory, best would be C:\ if does not inconvenience you.

Next step is adding it to your Environment variables if you wish it to   
run from any directory and not just where the program resides.
You may follow   
https://stackoverflow.com/a/75627861/22570293  
or   
https://www.computerhope.com/issues/ch000549.htm for a graphical representation.

If you installed sqlite3 in the C:\ directory and don't have a problem working in the terminal
use:
```terminal
setx PATH "%PATH%;C:\name of your sqlite folder"
```
This command works for other folders as well
```terminal
setx PATH "%PATH%;path in which sqlite resides"
```


