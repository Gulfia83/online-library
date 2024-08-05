# Сайт онлайн-библиотеки

С примером работы программы можно ознакомиться на GitHub Pages по ссылке: [https://gulena83.github.io/online-library-parser/](https://gulfia83.github.io/online-library/pages/index1.html)

## Как запустить

Клонируйте репозиторий. Установите зависимости:
```
pip install -r requirements.txt
```
Для просмотра загруженных книг запустите команду:
```
python render_website.py
```
## Описание

На сайте загружены книги из раздела научная фантастика.
Если необходимы другие книги их можно скачать в папку attachments воспользовавшись скриптом из репозитория [https://github.com/Gulfia83/online-library](https://github.com/Gulfia83/online-library). Инструкция по использованию скрипта есть в репозитории, нужно будет при запуске указать --dest_folder attachments.