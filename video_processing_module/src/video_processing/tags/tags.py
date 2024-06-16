"""Модуль содержащий класс предназначенный для обработки текста в теги"""

import json
from .tags_parser.computation import generate_tags


class Tags:
    """
    Класс для хранения компонентов видео (видео, аудио, описание) и URL-адреса видео.
    Позволяет генерировать JSON с тегами, разделенными по категориям с указанием их веса.

    Атрибуты:
        video_data (str): Текстовое представление видеоданных.
        audio_data (str): Текстовое представление аудиоданных.
        description_data (str): Текстовое описание видео.
        url (str): URL-адрес видео.

    Методы:
        set_video_data(data: str): Устанавливает текстовые данные видео.
        set_audio_data(data: str): Устанавливает текстовые данные аудио.
        set_description_data(data: str): Устанавливает текстовое описание видео.
        set_video_url(url: str): Устанавливает URL-адрес видео.
        generate_json() -> str: Генерирует JSON с тегами видео, аудио и описанием.
    """

    def __init__(self):
        self.video_data: str = None
        self.audio_data: str = None
        self.description_data: str = None
        self.url: str = None

    def set_video_data(self, data: str):
        """Устанавливает текстовое описание видеоряда"""
        self.video_data = data

    def set_audio_data(self, data: str):
        """Устанавливает транскрипцию аудио"""
        self.audio_data = data

    def set_description_data(self, data: str):
        """Устанавливает текст описания видео"""
        self.description_data = data

    def set_video_url(self, url: str):
        """Устанавливает ссылку на видео"""
        self.url = url

    def generate_json(self) -> str:
        """
        Генерирует JSON, содержащий информацию о видео, аудио, описании и URL.
        Теги группируются по категориям с указанием веса каждого тега.

        Возвращает:
            str: Строка в формате JSON с категоризированными тегами.
        """
        categories_data = generate_tags(
            self.video_data, self.audio_data, self.description_data
        )

        json_structure = {
            "video url": self.url,
            "categories": {},
            "quality": 1,
            "editing": 0
        }

        for category, tags in categories_data.items():
            json_structure["categories"][category] = {
                "tags": [{"tag": tag, "weight": weight} for tag, weight in tags.items()]
            }

        return json.dumps(json_structure, ensure_ascii=False)
