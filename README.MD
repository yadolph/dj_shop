### Дипломный проект "Интернет-магазин"

Порядок установки:
1. Скачать код c github, разарзивировать
2. Установить все пакеты:
 ```sh
pip install -r reqiurements.txt
```
3. Провести миграцию:
 ```sh
python manage.py migrate
```
4. Установить фикстуры:
 ```sh
python manage.py loaddata fixtures.json
```
5. Запустить сервер:
 ```sh
python manage.py runserver
```

админка находится по адресу http://127.0.0.1:8000/admin/
Имя пользователя - admin, пароль - admin