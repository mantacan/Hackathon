"""Модуль в котором содержится класс переводящий аудио в текст"""

import os
import subprocess
import tempfile
import whisper


class AudioProcessing:
    """
    Класс для обработки аудиодорожек из видеофайлов.

    Основная функция класса заключается в извлечении аудио из видео, конвертации его в формат WAV
    и последующем распознавании речи с помощью модели Whisper.

    Атрибуты:
        video (bytes): Байтовое представление видеофайла.
        audio_path (str): Путь к временному аудиофайлу в формате WAV.

    Методы:
        __init__(self, video): Конструктор класса, который принимает видео и инициирует его конвертацию в аудио.
        __convert_video_to_audio__(self): Приватный метод для конвертации видео в аудио.
        parse(self): Метод для распознавания речи из аудио и возвращения распознанного текста.
    """

    def __init__(self, video):
        self.video = video
        self.__convert_video_to_audio__()

    def __convert_video_to_audio__(self):
        """
        Конвертирует видео в аудио формат WAV, используя утилиту ffmpeg. В случае ошибок в процессе конвертации
        выбрасывает исключение с описанием ошибки.
        """
        print("Конвертация видео в аудио...")
        with tempfile.NamedTemporaryFile(suffix=".mp4", delete=False) as video_file:
            video_file.write(self.video)
            video_file.flush()
            output_audio_path = video_file.name + ".wav"
            command = [
                'ffmpeg',
                '-i', video_file.name,
                '-vn',
                '-acodec', 'pcm_s16le',
                '-ar', '44100',
                '-ac', '2',
                '-f', 'wav',
                output_audio_path
            ]
            process = subprocess.Popen(command, stderr=subprocess.PIPE)
            _, error = process.communicate()
            if process.returncode != 0:
                raise Exception("Ошибка при конвертации видео: " + str(error))
            print("Аудио успешно сконвертировано.")
            self.audio_path = output_audio_path

    def parse(self):
        """
        Загружает модель Whisper, использует её для распознавания речи из аудиофайла, удаляет временный аудиофайл
        и возвращает распознанный текст.
        """
        print("Загрузка модели Whisper...")
        model = whisper.load_model("base")
        print("Распознавание речи из аудио...")
        result = model.transcribe(self.audio_path)
        print("Распознавание завершено.")
        os.remove(self.audio_path)
        return result['text']
