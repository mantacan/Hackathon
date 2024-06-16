"""Модуль содержит класс переводящий видеоряд в текстовое описание используя локальный сервер"""

import requests
import re


def clean_text(text):
    """
    Очищает текст от нежелательных символов и пробелов.

    Аргументы:
        text (str): Исходный текст для очистки.

    Возвращает:
        str: Очищенный текст, где удалены все небуквенные символы кроме пробелов, и лишние пробелы сжаты.
    """
    cleaned_text = re.sub(r'[^a-zA-Z ]+', '', text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)
    cleaned_text = cleaned_text.strip()
    return cleaned_text


class VideoProcessing:
    """
    Класс для обработки видеофайлов путем отправки на сервер и получения текстового описания содержимого видео.

    Атрибуты:
        data (bytes): Байтовое представление видеофайла.
        server_url (str): URL сервера для отправки видеофайлов.

    Методы:
        __init__(self, data): Конструктор класса.
        parse(self): Отправляет видео на сервер и возвращает очищенное текстовое описание.
    """

    def __init__(self, data):
        self.server_url = 'http://localhost:8080/'
        self.data = data

    def parse(self):
        """Отправляет байты видео файла на сервер и получает описание."""
        files = {'file': ('placeholder.mp4', self.data)}
        try:
            response = requests.post(f"{self.server_url}/upload", files=files)
            response.raise_for_status()
            return clean_text(response.json()['success'][0]['output'])
        except Exception as e:
            print("Ошибка при отправке видео:", e)
