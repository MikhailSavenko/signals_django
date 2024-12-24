# Django Signals 
Проект создан в рамках изучения Сигналов Django. Этот проект демонстрирует использование сигналов Django для выполнения различных действий при сохранении, удалении и инициализации объектов модели. 

## Сигналы рассматриваются
post_save/pre_save
post_delete/pre_delete
pre_init/post_init

## Установка

1. Клонируйте репозиторий:
    ```sh
    git@github.com:MikhailSavenko/signals_django.git
    cd forecast
    ```

2. Установите зависимости:
    ```sh
    pip install -r requirements.txt
    ```

3. Настройте базу данных:
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

4. Создайте суперпользователя:
    ```sh
    python manage.py createsuperuser
    ```

5. Запустите сервер разработки:
    ```sh
    python manage.py runserver
    ```

## Использование
1. Перейдите в панель admin
2. Создайте User и Несколько Product
3. Изучите работу различных видов сигналов через методы и описаннные в них сценарии в файле signals
4. В apps.py добавлен метод ready для подключения сигналов(Так мы подключаем signals)