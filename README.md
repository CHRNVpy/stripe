# Тест пример интеграции платежного сервиса Stripe в Django

# Для запуска проекта локально необходимо клонировать данный репозиторий командой

```git clone https://github.com/CHRNVpy/stripe.git```

Перейти в каталог Stripe/, установить все зависимости

```pip install -r requirements.txt```

Запустить проект

```python manage.py runserver```

Затем в браузере использовать адреса:

127.0.0.1:8000/buy/1

127.0.0.1:8000/item/1


# Для запуска проекта c помощью Docker, необходимо установить docker https://docs.docker.com/desktop/install

В терминале(командной строке) сделать pull проекта командой

```docker pull chrnv/chrnvstripe```

Затем запустить проект командой

```docker run -p 8000:8000 chrnv/chrnvstripe```

Затем в браузере использовать адреса:

127.0.0.1:8000/buy/1

127.0.0.1:8000/item/1
