"""Класс обработки всех трех источников текста с последующей обработкой в json"""

import requests

from video_processing.tags import Tags
from .audio_parsing.audio_parser import AudioProcessing
from .video_parsing.video_parser import VideoProcessing


class Processing:
    """
    Класс для обработки видео- и аудиоданных, извлеченных из URL. Обеспечивает интеграцию и последовательную обработку
    видео и аудио компонентов, выдачу обработанных данных в формате тегов с помощью класса Tags.

    Атрибуты:
        request (str): URL видеофайла для скачивания и обработки.
        response (Tags): Экземпляр класса Tags для хранения и генерации тегов.
        video (bytes): Содержимое скачанного видео.

    Методы:
        download_video(): Скачивает видео по заданному URL. В случае ошибки загрузки выбрасывает исключение.
        process_video(): Обрабатывает видеоданные, используя класс VideoProcessing.
        process_audio(): Обрабатывает аудиоданные, используя класс AudioProcessing.
        process(): Инициирует полную обработку видео и аудио, а также подготовку данных к выводу в формате JSON.
    """

    def __init__(self, request: str):
        self.request = request
        self.download_video()
        self.response = Tags()

    def download_video(self):
        """Метод осуществляющий загрузку видео"""
        print("Загрузка видео...")
        response = requests.get(self.request, timeout=5)
        if response.status_code != 200:
            raise Exception("Ошибка загрузки видео")
        print("Видео успешно загружено.")
        self.video = response.content

    def process_video(self):
        """Обработка видеоряда"""
        self.response.set_video_data(VideoProcessing(self.video).parse())

    def process_audio(self):
        """Обработка аудиоряда"""
        self.response.set_audio_data(AudioProcessing(self.video).parse())

    def process(self):
        """
        Запускает полную обработку видео и аудио, включая извлечение данных и их форматирование.
        Возвращает экземпляр класса Tags с заполненными данными.
        """
        self.process_video()
        self.process_audio()
        return self.response
