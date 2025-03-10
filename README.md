# FirstDjango_01032025

## Инструкция по развертыванию проекта 

1. 'python3 -m venv django_venv'

2. 'source django_venv/bin/activate'

3. 'pip install -r requirements.txt'

4. 'python manage.py migrate'

5. 'python manage.py runserver'

## Запуск ipython  в контексте приложения 'django'
'''
python manage.py shell_plus --ipython
'''

## Выгрузки и загрузка данных из БД

### Выгрузить данные из БД.
'''
pythone manage.py dumpdata MainApp --ident 4 > ./fixtures/items.json
'''

### Загрузить данные в БД.

'''
pythone manage.py loaddata ./fixtures/items.json
'''

## дополнительно
1.Полезное дополнения для шаблонов Django.
'''
ext install batisteo.vscode-django
'''

Добавить в 'settings.json'

'''
"emmet.includeLanguages":{
    "django-html" : "html"
    },
"files.associations":{
        "*.html": "django-html"
    }
'''