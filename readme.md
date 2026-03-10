### 1. Подготовка базы данных
Генерация файлов миграций на основе моделей:



Применение миграций к базе данных:
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

2. Создание доступа
Создание аккаунта администратора:
```bash
python3 manage.py createsuperuser
```

3. Запуск приложения
Запуск локального сервера разработки:
```bash
python3 manage.py runserver```