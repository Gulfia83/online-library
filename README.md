# Online library website

You can see an example of the program on GitHub Pages at the link: [https://gulena83.github.io/online-library-parser/](https://gulfia83.github.io/online-library/pages/index1.html)

## How to run

Clone the repository. Install dependencies:
```
pip install -r requirements.txt
```
To view the downloaded books, run the command:
```
python render_website.py
```
By default, the program searches for data about books in the 'attachments/book_descriptions' folder.json' But you can specify your path by creating a .env file and saving the PATH_TO_DESCRIPTIONS variable containing the path to it.

Now you can use the library of books offline. To do this, follow the link [http://127.0.0.1:5500/pages/index1.html ](http://127.0.0.1:5500/pages/index1.html )

## Description

The site contains books from the science fiction section.
If you need other books, you can download them to the attachments folder using the script from the repository [https://github.com/Gulfia83/online-library](https://github.com/Gulfia83/online-library). Instructions for using the script are in the repository, you will need to specify --dest_folder attachments when running.