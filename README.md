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

[Ссылка на документацию](https://docs.google.com/document/d/1UeHJoez48fRU3JpK25Zym_Hco2By91AjhdsRWrNlYo8/edit?usp=sharing)
## Примеры

Пример работы с микросервисом обработки видео:
```
{
    "url": "https://cdn-st.rutubelist.ru/media/39/6c/b31bc6864bef9d8a96814f1822ca/fhd.mp4",
    "description": "A cat playing with a ball"
}
```
После отправки запроса на эндпоинт обработки, сервис обработает видео и аудио, сгенерирует теги и вернет результат в следующем формате:
```
{
    "message": "GOOD",
    "results": [
        {
            "id": "1",
            "tags": "{\"video url\": \"https://cdn-st.rutubelist.ru/media/39/6c/b31bc6864bef9d8a96814f1822ca/fhd.mp4\", \"categories\": {\"test\": {\"tags\": [{\"tag\": \"none\", \"weight\": 1}, {\"tag\": \"сейчас\", \"weight\": 1}, {\"tag\": \"тебе\", \"weight\": 1}, {\"tag\": \"покажу\", \"weight\": 1}, {\"tag\": \"секретную\", \"weight\": 1}, {\"tag\": \"команду\", \"weight\": 2}, {\"tag\": \"roblox\", \"weight\": 3}, {\"tag\": \"чтобы\", \"weight\": 2}, {\"tag\": \"её\", \"weight\": 2}, {\"tag\": \"активировать\", \"weight\": 1}, {\"tag\": \"поставь\", \"weight\": 1}, {\"tag\": \"лайк\", \"weight\": 1}, {\"tag\": \"подпишись\", \"weight\": 1}, {\"tag\": \"также\", \"weight\": 1}, {\"tag\": \"введев\", \"weight\": 1}, {\"tag\": \"чат\", \"weight\": 1}, {\"tag\": \"iloveyou\", \"weight\": 1}, {\"tag\": \"когда\", \"weight\": 1}, {\"tag\": \"вы\", \"weight\": 2}, {\"tag\": \"ведете\", \"weight\": 1}, {\"tag\": \"вас\", \"weight\": 1}, {\"tag\": \"на\", \"weight\": 1}, {\"tag\": \"экране\", \"weight\": 1}, {\"tag\": \"появится\", \"weight\": 1}, {\"tag\": \"вот\", \"weight\": 1}, {\"tag\": \"такой\", \"weight\": 1}, {\"tag\": \"clone\", \"weight\": 1}, {\"tag\": \"скрипт\", \"weight\": 1}, {\"tag\": \"был\", \"weight\": 1}, {\"tag\": \"создан\", \"weight\": 1}, {\"tag\": \"одним\", \"weight\": 1}, {\"tag\": \"из\", \"weight\": 2}, {\"tag\": \"создателей\", \"weight\": 1}, {\"tag\": \"работает\", \"weight\": 1}, {\"tag\": \"только\", \"weight\": 1}, {\"tag\": \"игре\", \"weight\": 1}, {\"tag\": \"где\", \"weight\": 1}, {\"tag\": \"есть\", \"weight\": 1}, {\"tag\": \"diva\", \"weight\": 1}, {\"tag\": \"loper\", \"weight\": 1}, {\"tag\": \"service\", \"weight\": 1}, {\"tag\": \"раскрымир\", \"weight\": 1}, {\"tag\": \"он\", \"weight\": 1}, {\"tag\": \"же\", \"weight\": 1}, {\"tag\": \"всего-то\", \"weight\": 1}, {\"tag\": \"выйти\", \"weight\": 1}, {\"tag\": \"игры\", \"weight\": 1}, {\"tag\": \"но\", \"weight\": 1}, {\"tag\": \"лучше\", \"weight\": 1}, {\"tag\": \"не\", \"weight\": 1}, {\"tag\": \"проверяй\", \"weight\": 1}, {\"tag\": \"cat\", \"weight\": 1}, {\"tag\": \"playing\", \"weight\": 1}, {\"tag\": \"ball\", \"weight\": 1}]}}, \"quality\": 1, \"editing\": 0}",
            "url": "https://cdn-st.rutubelist.ru/media/39/6c/b31bc6864bef9d8a96814f1822ca/fhd.mp4"
        }]
}
```
