import json
from jinja2 import Environment, FileSystemLoader, select_autoescape
from livereload import Server
from more_itertools import chunked

def on_reload():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html'])
    )
    template = env.get_template('template.html')

    with open('attachments/books_descriptions.json', 'r', encoding="utf8") as my_file:
        books_descriptions_json = json.load(my_file)

    books_descriptions = list(chunked(books_descriptions_json, 2))
    
    rendered_page = template.render(books_descriptions=books_descriptions)
    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)


def main():
    on_reload()
    server = Server()
    server.watch('template.html', on_reload)
    server.serve(root='.')


if __name__ == '__main__':
    main()
