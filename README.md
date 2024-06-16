# Сервис текстового поиска по медиаконтенту

## Обзор

Проект Обработки Видео состоит из двух микросервисов, предназначенных для обработки видеофайлов. Первый микросервис отвечает за обработку видео и аудиопотоков, генерацию тегов на основе контента, а также за возвращение результатов в структурированном формате JSON. Второй микросервис осуществляет поиск видеороликов по текстовому описанию. В проекте реализованы два эндпоинта: один для обработки видео и аудио, другой для поиска по текстовому описанию.

Проект интегрирован с Elasticsearch, который используется для индексации и поиска видеороликов. Эндпоинт обработки видео взаимодействует с сервисом Elasticsearch через ручку index, которая отправляет обработанные данные для индексации. Эндпоинт поиска использует ручку search для выполнения текстового поиска по проиндексированным видеороликам в Elasticsearch.

## Содержание

- [Обзор](#обзор)
- [Функциональные возможности](#функциональные-возможности)
- [Установка](#установка)
- [Использование](#использование)
- [Документация](#документация)
- [Примеры](#примеры)
## Функциональные возможности

- Генерация тегов на основе видео, аудио и описания пользователя
- Поиск видео по текстовому описанию
- Интеграция с Elasticsearch для индексации и поиска данных

## Установка

1. **Клонирование репозитория**
    ```bash
    git clone mantacan/Hackathon
    cd Hackathon
    ```

2. **Создание и активация виртуального окружения**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Установка зависимостей**
    ```bash
    pip install -r requirements.txt
    ```

4. **Загрузка данных NLTK**
    ```bash
    python -m nltk.downloader punkt stopwords
    ```

## Использование

### Запуск Flask приложения для микросервиса генерации тегов

1. **Установка переменной окружения**
    ```bash
    export PYTHONPATH="/path/to/project:$PYTHONPATH"
    ```

2. **Запуск Flask приложения**
    ```bash
    python3 app.py
    ```

## Документация

## Примеры

Пример работы с микросервисом обработки видео:
```
json

{
    "url": "https://cdn-st.rutubelist.ru/media/39/6c/b31bc6864bef9d8a96814f1822ca/fhd.mp4",
    "description": "A cat playing with a ball"
}
```
После отправки запроса на эндпоинт обработки, сервис обработает видео и аудио, сгенерирует теги и вернет результат в следующем формате:
```
json

{
    "id": "1",
    "url": "https://cdn-st.rutubelist.ru/media/39/6c/b31bc6864bef9d8a96814f1822ca/fhd.mp4",
    "tags": {
        "cat": 5,
        "ball": 4,
        "play": 3,
        "video_quality": 2
    }
}
```
