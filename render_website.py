import json
from jinja2 import Environment, FileSystemLoader, select_autoescape
from livereload import Server
from more_itertools import chunked
import os


BOOKS_ON_PAGE = 20
NUMBER_OF_COLUMNS = 2


def on_reload():
    path = os.getenv('PATH_TO_DESCRIPTIONS', default='attachments/books_descriptions.json')
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html'])
    )
    template = env.get_template('template.html')

    with open(path, 'r', encoding='utf8') as my_file:
        books_descriptions_json = json.load(my_file)

    books_descriptions = list(chunked(books_descriptions_json, BOOKS_ON_PAGE))
    pages_amount = len(books_descriptions)
    for page_number, books_on_page in enumerate(books_descriptions, 1):

        rendered_page = template.render(
            books_on_page=list(chunked(books_on_page, NUMBER_OF_COLUMNS)),
            pages_amount=pages_amount,
            page_number=page_number
        )

        os.makedirs('pages/', exist_ok=True)
        with open(os.path.join('pages/', f'index{page_number}.html'), 'w', encoding='utf8') as file:
            file.write(rendered_page)


def main():
    on_reload()
    server = Server()
    server.watch('template.html', on_reload)
    server.serve(root='.')


if __name__ == '__main__':
    main()
