import json
from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html'])
)
template = env.get_template('template.html')

with open('attachments/books_descriptions.json', 'r', encoding="utf8") as my_file:
    book_descriptions_json = my_file.read()

    books_descriptions = json.loads(book_descriptions_json)

rendered_page = template.render(books_descriptions=books_descriptions)
with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)